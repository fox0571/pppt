import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, DispatchForm
from request.forms import PartForm
from .models import Users
from request.models import UnitBasicInfo
# Create your views here.

def get_all_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).order_by('-callTime')
    return render(request, 'request/operator_list.html', {'request':request_list})
def get_all_dispatcher_records(request):
    code = request.session['user_code']
    request_list = UnitBasicInfo.objects.all().exclude(pre_diagnosis=None).filter(areaCode=code).filter(finished=True).order_by('-callTime')
    return render(request, 'request/dispatcher_list.html', {'request':request_list})
def get_all_scheduled_records(request):
    code = request.session['user_code']
    request_list = UnitBasicInfo.objects.all().exclude(pre_diagnosis=None).filter(areaCode=code).filter(finished=False).exclude(scheDate=None).order_by('-callTime')
    return render(request, 'request/dispatcher_list.html', {'request':request_list})
def get_new_records(request):
    code = request.session['user_code']
    request_list = UnitBasicInfo.objects.all().exclude(pre_diagnosis=None).filter(areaCode=code).filter(scheDate=None).order_by('-callTime')
    return render(request, 'request/dispatcher_list.html', {'request':request_list})

def get_all_oow_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).filter(warranty=False).order_by('-callTime')
    return render(request, 'request/operator_list.html', {'request':request_list})
def get_today_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).filter(callTime__gte=datetime.date.today()).order_by('-callTime')
    return render(request, 'request/operator_list.html', {'request':request_list})
def show_service_detail(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    form=DispatchForm()
    part_f=PartForm()
    return render(request, 'request/dispatch_detail.html', {'unit': unit,'form':form,'part_form':part_f})
def show_operator_page(request):
    name=request.session['user_name']
    a=UnitBasicInfo.objects.all().filter(receiver=name).filter(callTime__gte=datetime.date.today()).count()
    b=UnitBasicInfo.objects.all().filter(receiver=name).filter(warranty=False).count()
    c=UnitBasicInfo.objects.all().filter(receiver=name).count()
    return render(request, 'request/dashboard_op.html',{'today':a,'oow':b,'all':c})
def show_dispatcher_page(request):
    name=request.session['user_name']
    code = request.session['user_code']
    user = Users.objects.get(code=code)
    a=UnitBasicInfo.objects.all().filter(areaCode=code).filter(scheDate=None).count()
    b=UnitBasicInfo.objects.all().filter(areaCode=code).filter(finished=False).exclude(scheDate=None).count()
    c=UnitBasicInfo.objects.all().filter(areaCode=code).filter(finished=True).count()

    print (request.session['user_group'])
    return render(request, 'request/dashboard_dp.html',{'new':a,'sche':b,'fin':c})
def show_page(request):
    group = request.session['user_group']
    if group=="dispatcher":
        return redirect('/user/dispatcher/')
    if group=="operator":
        return redirect('/user/operator/')
    if group=="warranty":
        return redirect('/warranty/')
    if group=="admin":
        return redirect('/admin/')
    print (request.session['user_group'])
    return render(request, 'request/dashboard_dp.html',{'new':a,'sche':b,'fin':c})
def login(request):
    message=""
    if request.session.get('is_login',None):
        return redirect('/user/')
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            code = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            try:
                user = Users.objects.get(code=code)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_code'] = user.code
                    request.session['user_name'] = user.name
                    group=user.group
                    request.session['user_group'] = group
                    return redirect('/user/')
                else:
                    message = "Wrong password!"
            except:
                message = "No such a user!"
    form=LoginForm()
    return render(request, 'request/login.html',{'form':form,'message':message})

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/request/")
    request.session.flush()
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/user/login/")
