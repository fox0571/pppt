import datetime
from django.shortcuts import render, redirect, get_object_or_404
from request.models import UnitBasicInfo
from django.utils import timezone
from .forms import WarrantyForm

def showAll(request):
    allWarranties=UnitBasicInfo.objects.filter(warranty=None)
    return render(request, 'request/warranty.html', {'requests':allWarranties})

def showDetail(request,pk):
    warranty = get_object_or_404(UnitBasicInfo, pk=pk)
    form=WarrantyForm()
    return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})

def update(request,pk):
    if request.method == "POST":
        form=WarrantyForm(request.POST)
        if form.is_valid():
            warranty=form.cleaned_data["warranty"]
            note=form.cleaned_data["warrantyNote"]
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        unit.warranty=warranty
        unit.warrantyNote=note
        unit.save()
        return redirect('/warranty/')
    else:
        return render(request, 'request/warranty_detail.html', {'unit': warranty,'form':form})
