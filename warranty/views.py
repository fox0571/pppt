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
from django.contrib.auth.models import User
import unicodecsv
from django.http import HttpResponse, JsonResponse


# this view is for datatable

DEFAULT_START_POSITION = 0
DEFAULT_PAGE_SIZE = 10
DEFAULT_SORTING_COLUMN_INDEX = 1
DEFAULT_SORTING_METHOD = 'asc'

#constants for querying
ORDER_DICT = {
    0: 'field1',
    1: 'field2',
}

ORDER_BY = {
    'desc': '-',
    'asc': ''
}

QUERY_FIELDS = ['field1', 'field2']
def get_sorting(request_values):
    return int(request_values.get('order[0][column]', DEFAULT_SORTING_COLUMN_INDEX)),\
           request_values.get('order[0][dir]', DEFAULT_SORTING_METHOD).lower()

def get_paging(request_values):
    return int(request_values.get('start', DEFAULT_START_POSITION)),\
               int(request_values.get('length', DEFAULT_PAGE_SIZE))

def render_records(current_page_members, query):
    # list to be returned for data
    records = []
    for q in current_page_members:
        dic={}
        for field_name in q._meta.get_fields() :
            fn=field_name.attname
            if fn=="invoice":
                invoice_dic={}
                invoice_dic["number"]=getattr(q, fn)
                invoice_dic["link"]="/request/invoice/approve/"+str(getattr(q, "id"))+"/"
                dic[fn]=invoice_dic
            else:
                value = getattr(q, field_name.attname)
                dic[field_name.attname]=str(value)
        records.append(dic)
    return records
    
def get_member_list(request_values,query,sort_by,sort_column,page_size):
    col_index=sort_column
    col="columns["+str(col_index)+"][data]"
    field_name=request_values.get(col,"")
    order=ORDER_BY[sort_by]+field_name
    index=request_values.get("start","1")
    invoice_type=request_values.get("type","")
    all_invoices=Invoice.objects.all().order_by(order)
    if invoice_type=="0":
        all_invoices=all_invoices.filter(status=0)
    elif invoice_type == "1":
        all_invoices=all_invoices.filter(status=1)
    elif invoice_type == "2":
        all_invoices=all_invoices.filter(status=2)
    
    if query:
        all_records=all_invoices.filter(
            Q(invoice__icontains=query)|
            Q(incident__sksid=query)|
            Q(incident__techName__icontains=query)|
            Q(voucher=query)
        )
    else:
        all_records=all_invoices
    
    filter_count=all_records.count()
    paginator = Paginator(all_records,page_size)
    page = int(index)/page_size+1
    current_page_records = paginator.get_page(page)
    return all_records, int(filter_count), current_page_records

def get_invoice(request):
    # ... receive the request
    request_values = request.GET
    # paging
    start, page_size = get_paging(request_values)
    # sorting
    sort_column, sort_by = get_sorting(request_values)
    draw=request_values.get("draw",99)

    # research query
    query = request_values.get('search[value]', '')  # get search term from datatable request
    #query_combined = self.get_combined_query(query)

    all_records, filter_count, current_page_records = \
        get_member_list(request_values, query, sort_by, sort_column, page_size)

    # json dict to be returned
    records = {
        'recordsTotal': all_records.count(),    # The total count of records in your database, if query exist, it is the count of filtered records
        'recordsFiltered': filter_count,
        'draw': draw,    # Represents the rendering count of datatable
        'data': [],    # Main data to be rendered in table
        'error':'',
    }

    # if no query, all records returned
    records.update({'recordsFiltered': filter_count if query else records['recordsTotal']})

    # update aaData list for records
    records['data'].extend(render_records(current_page_records, query))

    return JsonResponse(records)
def invoice_datatable(request):
    tp=request.GET.get("type","")
    return render(request, 'stat/service_daily.html',{"type":tp})

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
        if d.active and int(d.code)<7:
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
    new=invoices.filter(status=0).count()
    w9=invoices.filter(need_w9=True).count()
    finished=invoices.filter(processed=True).count()
    dispute=invoices.filter(status=2).count()
    all=invoices.count()
    inhouse=invoices.filter(invoice_type=1).count()
    approved=invoices.filter(status=1).filter(processed=False).filter(need_w9=False).filter(invoice_type=0).count()
    para = {
        'new':new,
        'finished':finished,
        'all':all,
        'dispute':dispute,
        'w9':w9,
        'inhouse':inhouse,
        'approved':approved,
    }
    # if request.user.username == "sksap":
    #     return render(request, 'account/ap_dashboard.html',para)
    # else:
    return render(request, 'account/ap_dashboard.html',para)
def invoice_waiting(request):
    invoices=Invoice.objects.all().filter(processed=False).filter(need_w9=False).exclude(status=3).order_by("-pk")
    return render(request, 'account/invoices_process_list.html',{'invoices':invoices})

def invoices(request):
    invoices=Invoice.objects.all().order_by("-pk")
    invoice_type=request.GET.get("type","")
    
    if invoice_type == "0":     #waiting invoices
        new=invoices.filter(status=0)
        return render(request, 'account/invoices.html',{'invoices':new})
    elif invoice_type == "1":    #approval invoices
        approval=invoices.filter(status=1).filter(processed=False).filter(need_w9=False)
        return render(request, 'account/invoices.html',{'invoices':approval})
    elif invoice_type == "2":    #disputed invoices
        disputed=invoices.filter(status=2)
        return render(request, 'account/invoices.html',{'invoices':disputed})
    elif invoice_type == "3":    #need W_9 invoices
        w9=invoices.filter(need_w9=True)
        return render(request, 'account/invoices.html',{'invoices':w9})
    elif invoice_type == "4":   #invoice from inhouse tech
        inhouse=invoices.filter(invoice_type=1)
        return render(request, 'account/invoices.html',{'invoices':inhouse})
    else:
        invoices=Invoice.objects.all().order_by("-pk")

        search_text=request.GET.get("search","")
        if search_text:
            invoices=invoices.filter(
                Q(sksid__icontains=search_text)|
                Q(invoice__icontains=search_text)|
                Q(voucher__icontains=search_text)
                #Q(incident__icontains=search_text)
            )
        paginator = Paginator(invoices, 50)

        page = request.GET.get('page')
        invoice = paginator.get_page(page)

        return render(request, 'account/invoices.html',{'invoices':invoice})
        #return JsonResponse({"ERROR":"Wrong Type"})


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

    search_text=request.GET.get("search","")
    if search_text:
        invoices=invoices.filter(
            Q(sksid__icontains=search_text)|
            Q(invoice__icontains=search_text)|
            Q(voucher__icontains=search_text)
            #Q(incident__icontains=search_text)
        )
    paginator = Paginator(invoices, 50)

    page = request.GET.get('page')
    invoice = paginator.get_page(page)

    return render(request, 'account/invoices.html',{'invoices':invoice})
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
            #for inhouse invoice
            if "inhouse" in request.POST:
                new_invoice.invoice_type = 1
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
    files = unit.filesimplemodel_set.all()
    if request.method == "POST":
        form=WarrantyForm(request.POST,instance=unit)
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
            month=datetime.datetime.now().month
            year=datetime.datetime.now().year
            area=unit.location_state
            #code = random.randint(1,4)
            unit.warranty=warranty
            unit.warrantyNote=note
            if unit.sksid == None:
                code=get_code()
                unit.areaCode=code
                # dispatcher=User.objects.get(pk=(code+23))
                # unit.dispatcher=dispatcher
                #if under warranty:
                if code != -1 :
                    new_id=new_sksid(month,year,code)
                    unit.sksid=new_id
                    dispatcher=User.objects.get(pk=(str(int(code)+23)))
                    unit.dispatcher=dispatcher
            unit.pre_diagnosis_flag=True
            unit.save()
            return redirect('/warranty/')
        return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form,'files':files})
    form=WarrantyForm(instance=unit)
    return render(request, 'request/warranty_detail.html', {'unit': unit,'form':form,'files':files})

def export_all_invoices_as_csv(request):
    fields=["Invoice","Ref","Total Cost","Tech","Status","Voucher"]
    opts = Invoice._meta
    if not fields:
        field_names = [field.name for field in opts.fields]
    else:
        field_names = fields

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

    writer = unicodecsv.writer(response, encoding='utf-8')

    queryset=Invoice.objects.all()
    writer.writerow(field_names)
    for obj in queryset:
        row=[]
        row.append(obj.invoice)
        row.append(obj.incident.sksid)
        row.append(obj.total_c)
        row.append(obj.incident.techName)
        if obj.need_w9:
            row.append("NEED W-9")
        elif obj.status==1:
            row.append("APPROVED")
        elif obj.status==2:
            row.append("DISPUTED")
        else:
            row.append("WAITING")
        row.append(obj.voucher)
        writer.writerow(row)
    return response