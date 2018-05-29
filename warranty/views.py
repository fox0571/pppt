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

def update(request,pk):
    if request.method == "POST":
        form=WarrantyForm(request.POST)
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        print(unit.location_zip)
        month=unit.callTime.month
        year=unit.callTime.year
        area=unit.location_state
        print (area,pk,month)
        code = get_code(area)
        unit.warranty=warranty
        unit.warrantyNote=note
        unit.areaCode=code
        print (code)
        user=get_object_or_404(Users, code=code)
        task=user.current_tasks
        mon=user.current_month
        if month==mon:
            task=task+1
            user.current_tasks=task
        else:
            task=1
            user.current_tasks=task
            if mon==12:
                user.current_month=1
            else:
                user.current_month=mon+1
        m=""
        if month<10:
            m="0"+str(month)
        else:
            m=str(month)
        sksid="SKS"+m+str(year)+"-D"+str(code)+"-"+str(task)
        unit.sksid=sksid
        unit.save()
        return redirect('/warranty/')
    else:
        return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})
