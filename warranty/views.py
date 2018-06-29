import datetime
from django.shortcuts import render, redirect, get_object_or_404
from request.models import UnitBasicInfo
from users.models import Users
from django.utils import timezone
from .forms import WarrantyForm, AccountForm
from .models import Invoice

#show all serial numbers
def show_all(request):
    all=UnitBasicInfo.objects.all()
    return render(request, 'request/warranty.html', {'requests':all})

#show all unverified serial numbers
def show_waiting(request):
    all=UnitBasicInfo.objects.filter(warranty=None)
    return render(request, 'request/warranty.html', {'requests':all})

def show_detail(request,pk):
    warranty = get_object_or_404(UnitBasicInfo, pk=pk)
    form=WarrantyForm()
    return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})

def get_code(area):
    #(1,"Jane"),(2,"Yesi"),(3,"Chloe"),(4,"Christina"),(5,"Daniela"),(6,"Samantha")
    LIST_6=['CA','AZ','NV','UT','ID','CO']
    LIST_4=['WA','OR','MT','WY','NM','ND','SD','NE','KS','MN','IA','AR']
    LIST_2=['TX','OK','LA','MS']
    LIST_1=['GA','FL']
    LIST_3=['WI','MO','IL','MI','IN','OH','KY','TN','AL']
    LIST_5=['ME','VT','NH','MA','CT','RI','NY','PA','NJ','DE','MD','DC','WV','VA','NC','SC']
    for st in LIST_1:
        if st==area:
            return 1
    for st in LIST_2:
        if st==area:
            return 2
    for st in LIST_3:
        if st==area:
            return 3
    for st in LIST_4:
        if st==area:
            return 4
    for st in LIST_5:
        if st==area:
            return 5
    for st in LIST_6:
        if st==area:
            return 6
def reg_month(month):
    if month<10:
        return "0"+str(month)
    else:
        return str(month)
def ac_list(request):
    unit=UnitBasicInfo.objects.all()
    return render(request, 'account/list.html',{'unit':unit})
def invoice_list(request):
    invoices=Invoice.objects.all().order_by("-pk")
    return render(request, 'account/invoices.html',{'invoices':invoices})
def invoice_edit(request,pk):
    invoice=get_object_or_404(Invoice,pk=pk)
    if request.method == "POST":
        form=AccountForm(request.POST,instance=invoice)
        if form.is_valid():
            invoice=form.save(commit=False)
            tot=(invoice.travel_c
                +invoice.labor_c
                +invoice.material_c)
            invoice.total_c=tot
            invoice.save()
            return redirect("/warranty/account/invoice/")
    else:
        form=AccountForm(instance=invoice)
    return render(request, 'account/invoice_edit.html',{'form':form})
def account(request,pk):
    form=AccountForm()
    unit=get_object_or_404(UnitBasicInfo,pk=pk)
    inv=Invoice.objects.all().filter(sksid=unit.sksid)
    if request.method == "POST":
        new_invoice=Invoice()
        form=AccountForm(request.POST,instance=new_invoice)
        if form.is_valid():
            new_invoice = form.save(commit=False)
            tot=(new_invoice.travel_c
                +new_invoice.labor_c
                +new_invoice.material_c)
            new_invoice.sksid=unit.sksid
            new_invoice.total_c=tot
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
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
            month=unit.callTime.month
            year=unit.callTime.year
            area=unit.location_state
            code = get_code(area)
            unit.warranty=warranty
            unit.warrantyNote=note
            unit.areaCode=code
            #if under warranty:
            new_id=new_sksid(month,year,code)
            unit.sksid=new_id
            unit.save()
            return redirect('/warranty/')
        return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form})
    form=WarrantyForm(instance=unit)
    return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form})
