import datetime
from django.shortcuts import render, redirect
from .models import Request, CheckForm, Partsinv
from django.utils import timezone
from .forms import RequestForm, BasicInfoForm

def req_new(request):
    form=RequestForm()
    return render(request, 'request/request_new.html',{'form': form})
def basic_info(request):
    form=BasicInfoForm()
    return render(request, 'request/basicinfo.html',{'form': form})
def dashboard_op(request):
    return render(request, 'request/dashboard_op.html')
def submit(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        post = form.save()
        post.requestTime = timezone.now()
        post.save()
        return redirect('/request/all')
    else:
        form = RequestForm()

def available(request):
    form=CheckForm()
    return render(request, 'request/check.html',{'form': form})

def submita(request):

    form = CheckForm(request.POST)
    query = request.POST.get('number','0')
    print(query)
    result=Partsinv.objects.get(number=query)
    return render(request, 'request/availability.html', {'request':result})


def showAllRequests(request):
    request_list = Request.objects.order_by('-requestTime')
    return render(request, 'request/request_detail.html', {'request':request_list})

def showPendingRequests(request):
    request_list = Request.objects.filter(requestStatue=False)
    return render(request, 'request/request_detail.html', {'request':request_list})

def showFinishedRequests(request):
    request_list = Request.objects.filter(requestStatue=True)
    return render(request, 'request/request_detail.html', {'request':request_list})
