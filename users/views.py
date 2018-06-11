import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, DispatchForm, ChangePassword
from request.forms import PartForm
from .models import Users
from request.models import UnitBasicInfo, PartRequest
# Create your views here.

#show all unverified serial numbers
def show_waiting(request):
    all=UnitBasicInfo.objects.filter(warranty=None)
    return render(request, 'request/warranty.html', {'requests':all})
def get_all_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).order_by('-callTime')
    return render(request, 'operator/list.html', {'request':request_list})
def get_all_dispatcher_records(request):
    code = request.session['user_code']
    request_list = UnitBasicInfo.objects.all().exclude(pre_diagnosis=None).filter(areaCode=code).filter(finished=True).order_by('-callTime')
    return render(request, 'dispatcher/list.html', {'request':request_list})
def get_all_scheduled_records(request):
    code = request.session['user_code']
    request_list = UnitBasicInfo.objects.all().exclude(pre_diagnosis=None).filter(areaCode=code).filter(finished=False).exclude(scheDate=None).order_by('-callTime')
    return render(request, 'dispatcher/list.html', {'request':request_list})
def get_new_records(request):
    code = request.session['user_code']
    print(code)
    request_list = UnitBasicInfo.objects.all().filter(warranty=True).filter(areaCode=code).filter(scheDate=None).order_by('-callTime')
    return render(request, 'dispatcher/list.html', {'request':request_list})
def get_all_part_records(request):
    code = request.session['user_code']
    request_list = PartRequest.objects.all().filter(code=code).order_by('-request_time')
    return render(request, 'dispatcher/part_list.html', {'request':request_list})
def get_all_oow_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).filter(warranty=False).order_by('-callTime')
    return render(request, 'operator/list.html', {'request':request_list})
def get_today_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).filter(callTime__gte=datetime.date.today()).order_by('-callTime')
    return render(request, 'operator/list.html', {'request':request_list})
def show_follow_up(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    return render(request, 'dispatcher/followup.html', {'unit': unit})
def show_service_detail(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    form=DispatchForm()
    return render(request, 'dispatcher/tech.html', {'unit': unit,'form':form})
def show_operator_page(request):
    name=request.session['user_name']
    a=UnitBasicInfo.objects.all().filter(receiver=name).filter(callTime__gte=datetime.date.today()).count()
    b=UnitBasicInfo.objects.all().filter(receiver=name).filter(warranty=False).count()
    c=UnitBasicInfo.objects.all().filter(receiver=name).count()
    return render(request, 'operator/dashboard.html',{'today':a,'oow':b,'all':c})
def show_dispatcher_page(request):
    name=request.session['user_name']
    code = request.session['user_code']
    user = Users.objects.get(code=code)
    a=UnitBasicInfo.objects.all().filter(areaCode=code).filter(scheDate=None).count()
    b=UnitBasicInfo.objects.all().filter(areaCode=code).filter(finished=False).exclude(scheDate=None).count()
    c=UnitBasicInfo.objects.all().filter(areaCode=code).filter(finished=True).count()
    d=PartRequest.objects.all().filter(code=code).count()
    return render(request, 'dispatcher/dashboard.html',{'new':a,'sche':b,'fin':c,'parts':d})
def show_admin_page(request):
    units=UnitBasicInfo.objects.all().order_by('-callTime')
    return render(request, 'admin/admin.html',{'reqeust':units})
def show_page(request):
    group = request.session['user_group']
    if group=="dispatcher":
        return redirect('dispatcher/')
    if group=="operator":
        return redirect('operator/')
    if group=="warranty":
        return redirect('warranty/')
    if group=="adminop":
        return redirect('/request/adminop/')
    if group=="admindp":
        return redirect('/request/admindp/')
    if group=="admin":
        return redirect('/user/admin/')
    if group=="parts":
        return redirect('/request/part/')
    return render(request, 'dispatcher/dashboard.html',{'new':a,'sche':b,'fin':c})
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
                    print(group)
                    return redirect('/user/')
                else:
                    message = "Wrong password!"
            except:
                message = "No such a user!"
    form=LoginForm()
    return render(request, 'request/login.html',{'form':form,'message':message})

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/user/login/")
    request.session.flush()
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/user/login/")
def change_password(request):
    form1=ChangePassword()
    message=""
    if not request.session.get('is_login',None):
        return redirect('login/')
    if request.method == "POST":
        form = ChangePassword(request.POST)
        if form.is_valid():
            old_password=form.cleaned_data['old_pw'];
            new_password=form.cleaned_data['new_pw'];
            new_password2=form.cleaned_data['new_pw2'];
            user=Users.objects.get(code=request.session['user_code'])
            if old_password != user.password:
                message="The current password is not correct"
            else:
                if new_password != new_password2:
                    message="The new passwords are not the same"
                else:
                    message="success"
                    user.password=new_password
                    user.save()
    return render(request,'request/change.html',{'form':form1,'message':message})
