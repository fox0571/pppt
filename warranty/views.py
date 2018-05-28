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
    LIST_1=['FL','SC']
    LIST_2=['TX','LA']
    LIST_3=['IL','WI']
    LIST_4=['WA','OR']
    LIST_5=['MA','ME']
    LIST_6=['CA','AZ']
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
        month=unit.callTime.month
        year=unit.callTime.year
        area=unit.location_state
        code = get_code(area)
        unit.warranty=warranty
        unit.warrantyNote=note
        unit.areaCode=code

        user=get_object_or_404(User, code=code)
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
