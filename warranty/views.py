import datetime
from django.shortcuts import render, redirect, get_object_or_404
from request.models import UnitBasicInfo
from users.models import Users
from django.utils import timezone
from .forms import WarrantyForm

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
    LIST_1=['CA','AZ','NV','UT','ID','CO']
    LIST_2=['WA','OR','MT','WY','NM','ND','SD','NE','KS','MN','IA','AR']
    LIST_3=['TX','OK','LA','MS']
    LIST_4=['GA','FL']
    LIST_5=['WI','MO','IL','MI','IN','OH','KY','TN','AL']
    LIST_6=['ME','VT','NH','MA','CT','RI','NY','PA','NJ','DE','MD','DC','WV','VA','NC','SC']
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
def generate_default_sksid(month,year,code):
    return "SKS"+ reg_month(month)+str(year)+"-"+"D"+str(code)+"-1"
def update(request,pk):
    if request.method == "POST":
        form=WarrantyForm(request.POST)
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
        unit=get_object_or_404(UnitBasicInfo, pk=pk)

        #improve the way generate the sksid

        month=unit.callTime.month
        year=unit.callTime.year
        area=unit.location_state
        code = get_code(area)
        unit.warranty=warranty
        unit.warrantyNote=note
        unit.areaCode=code
        last_unit=UnitBasicInfo.objects.filter(areaCode=code).order_by('-id')
        sks=""
        month1=0
        new_sks=""
        if len(last_unit)!=0:
            last_unit=last_unit[0]
            month1=last_unit.callTime.Month
            year1=last_unit.callTime.year
            sks=last_unit.sksid.split("-")
            sks_pre=sks[0]
            sks_middle="D"+str(code)
            sks_last=sks[2]
            if month1==month:
                new_sks=sks_pre+"-"+sks_middle+"-"+str(1)
            else:
                if month==1:
                    sks_pre="SKS01"+str(year)
                    new_sks=sks_pre+"-"+sks_middle+"-"+str(int(sks_last)+1)
                else:
                    sks_pre="SKS"+reg_month(month)+str(year)
                    new_sks=sks_pre+"-"+sks_middle+"-"+str(int(sks_last)+1)
        else:
            new_sks=generate_default_sksid(month,year,code)
        unit.sksid=new_sks
        unit.save()
        return redirect('/warranty/')
    else:
        return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})
