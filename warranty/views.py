import datetime
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, redirect, get_object_or_404
from request.models import UnitBasicInfo
from users.models import Users
from django.utils import timezone
from .forms import WarrantyForm, AccountForm
from .models import Invoice
import random

#show all serial numbers
def show_all(request):
    all=UnitBasicInfo.objects.all()
    return render(request, 'request/warranty.html', {'requests':all})

def show_waiting(request):
    all=UnitBasicInfo.objects.filter(warranty=None)
    return render(request, 'request/warranty.html', {'requests':all})

def show_detail(request,pk):
    warranty = get_object_or_404(UnitBasicInfo, pk=pk)
    form=WarrantyForm()
    return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})
def get_active_dispatchers():
    all_dispatchers=Users.objects.filter(group="dispatcher")
    active_list=[]
    for d in all_dispatchers:
        if d.active and int(d.code)<5:
            active_list.append(d.code)
    return active_list
def get_code():
    active_list=get_active_dispatchers()
    p=random.randint(0,len(active_list)-1)
    return (active_list[p])
def reg_month(month):
    if month<10:
        return "0"+str(month)
    else:
        return str(month)
def ac_list(request):
    unit_list=UnitBasicInfo.objects.all()
    search_text=request.GET.get("search","")
    if search_text:
        unit_list=unit_list.filter(
            Q(sksid__icontains=search_text)|
            Q(businessName__icontains=search_text)|
            Q(serialNumber__icontains=search_text)|
            Q(techName__icontains=search_text)
        )
    paginator = Paginator(unit_list, 50)

    page = request.GET.get('page')
    unit = paginator.get_page(page)
    return render(request, 'account/list.html',{'unit':unit})
def invoice_dashboard(request):
    invoices=Invoice.objects.all()
    new=invoices.filter(processed=False).filter(need_w9=False).count()
    w9=invoices.filter(need_w9=True).count()
    finished=invoices.filter(processed=True).count()
    dispute=invoices.filter(status=2).count()
    all=invoices.count()
    para = {
        'new':new,
        'finished':finished,
        'all':all,
        'dispute':dispute,
        'w9':w9,
    }
    return render(request, 'account/invoice_dashboard.html',para)
def invoice_waiting(request):
    invoices=Invoice.objects.all().filter(processed=False).filter(need_w9=False).order_by("-pk")
    return render(request, 'account/invoices_process_list.html',{'invoices':invoices})
def invoice_processed(request):
    invoices=Invoice.objects.all().filter(processed=True).order_by("-pk")
    return render(request, 'account/invoices.html',{'invoices':invoices})
def invoice_disputed(request):
    invoices=Invoice.objects.all().filter(status=2).order_by("-pk")
    return render(request, 'account/invoices.html',{'invoices':invoices})
def invoice_w9(request):
    invoices=Invoice.objects.all().filter(need_w9=True).order_by("-pk")
    return render(request, 'account/invoices.html',{'invoices':invoices})
def invoice_all(request):
    invoices=Invoice.objects.all().order_by("-pk")
    return render(request, 'account/invoices.html',{'invoices':invoices})
def invoice_pro(request,pk):
    invoice=get_object_or_404(Invoice,pk=pk)
    invoice.processed=True
    invoice.save()
    return redirect("/warranty/account/invoice/new/")
def invoice_edit(request,pk):
    invoice=get_object_or_404(Invoice,pk=pk)
    origin_tot=invoice.total_c
    if request.method == "POST":
        form=AccountForm(request.POST,request.FILES,instance=invoice)
        if form.is_valid():
            invoice=form.save(commit=False)
            tot=(invoice.travel_c
                +invoice.labor_c
                +invoice.material_c)
            invoice.total_c=tot
            if origin_tot!=tot:
                invoice.status=0
            invoice.save()
            return redirect("/warranty/account/invoice/")
    else:
        form=AccountForm(instance=invoice)
    return render(request, 'account/invoice_edit.html',{'form':form,'invoice':invoice})
def account(request,pk):
    form=AccountForm()
    unit=get_object_or_404(UnitBasicInfo,pk=pk)
    inv=Invoice.objects.all().filter(sksid=unit.sksid)
    if request.method == "POST":
        new_invoice=Invoice()
        form=AccountForm(request.POST,request.FILES,instance=new_invoice)
        if form.is_valid():
            new_invoice = form.save(commit=False)
            tot=(new_invoice.travel_c
                +new_invoice.labor_c
                +new_invoice.material_c)
            new_invoice.sksid=unit.sksid
            new_invoice.total_c=tot
            new_invoice.incident=unit
            new_invoice.save()
            return redirect("#/")
        return render(request, 'account/rate.html',{'form':form,'unit':unit,'invoices':inv})
    return render(request, 'account/rate.html',{'form':form,'unit':unit,'invoices':inv})
def new_sksid(m,y,code):
    id=""
    user=get_object_or_404(Users, code=code)
    c_t=user.current_tasks
    c_m=user.current_month
    if m==c_m:
        user.current_tasks=c_t+1
        id="SKS"+ reg_month(m)+str(y)+"-D"+str(code)+"-"+str(user.current_tasks)
    else:
        user.current_tasks=1
        if c_m==12:
            user.current_month=1
            id="SKS01"+str(y+1)+"-D"+str(code)+"-"+str(user.current_tasks)
        else:
            user.current_month=m
            id="SKS"+ reg_month(m)+str(y)+"-D"+str(code)+"-"+str(user.current_tasks)
    user.save()
    return id
def update_warranty(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    if request.method == "POST":
        form=WarrantyForm(request.POST,instance=unit)
        print (unit)
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
            month=datetime.datetime.now().month
            year=datetime.datetime.now().year
            area=unit.location_state
            code = get_code()
            #code = random.randint(1,4)
            unit.warranty=warranty
            unit.warrantyNote=note
            unit.areaCode=code
            #if under warranty:
            if code != -1:
                new_id=new_sksid(month,year,code)
                unit.sksid=new_id
            unit.pre_diagnosis_flag=True
            unit.save()
            return redirect('/warranty/')
        return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form})
    form=WarrantyForm(instance=unit)
    return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form})
