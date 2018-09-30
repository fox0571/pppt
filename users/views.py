import datetime
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, DispatchForm, ChangePassword
from request.forms import PartForm, FirstForm
from .models import Users
from request.models import UnitBasicInfo, PartRequest
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#show all unverified serial numbers
OPERATOR_GROUP=["Anna","Brandon","Jackie","Randi","Christina","Amanda Gomez","Etnia"]

@login_required(login_url='/user/login/')
@permission_required('users.change_user_status',raise_exception=True)
def manage_queue(request):
    dispatchers=Users.objects.filter(group='dispatcher')
    active_dispatchers=dispatchers.filter(active=True)
    inactive_dispatchers=dispatchers.filter(active=False)
    if request.method == "POST":
        activedispatchers=request.POST.getlist('left')
        inactivedispatchers=request.POST.getlist('right')
        if activedispatchers:
            for d in activedispatchers:
                dispatcher=get_object_or_404(Users,pk=d)
                dispatcher.active=True
                dispatcher.save()
        if inactivedispatchers:
            for d in inactivedispatchers:
                dispatcher=get_object_or_404(Users,pk=d)
                dispatcher.active=False
                dispatcher.save()
        dispatchers=Users.objects.filter(group='dispatcher')
        active_dispatchers=dispatchers.filter(active=True)
        inactive_dispatchers=dispatchers.filter(active=False)        
    return render(request, 'dispatcher/queue.html',{'ad':active_dispatchers,'iad':inactive_dispatchers})
def show_detail_op(request,pk):
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    form = FirstForm(instance=unit)
    return render(request, 'operator/basic.html', {'form':form})
def show_waiting(request):
    all=UnitBasicInfo.objects.filter(warranty=None)
    return render(request, 'request/warranty.html', {'requests':all})
def get_all_records(request):
    name=request.session['user_name']
    request_list = UnitBasicInfo.objects.all().filter(receiver=name).order_by('-callTime')
    return render(request, 'operator/list.html', {'request':request_list})
def get_all_dispatcher_records(request):
    code = request.session['user_code']
    my_tasks=""
    if code=="17":
        # my_tasks=UnitBasicInfo.objects.filter(
        #     Q(location_state='TX') | 
        #     Q(location_state='CA') |
        #     Q(location_state='LA') |
        #     Q(location_state='OK')).filter(inhouse=True)
        my_tasks=UnitBasicInfo.objects.filter(inhouse=True)
    elif code=="18":
        my_tasks=UnitBasicInfo.objects.filter(
            Q(location_state='MA') |
            Q(location_state='NJ') |
            Q(location_state='NH') |
            Q(location_state='CT') |
            Q(location_state='PA') |
            Q(location_state='VT') |
            Q(location_state='ME') |
            Q(location_state='RI') |
            Q(location_state='NY') |
            Q(location_state='DE')).filter(inhouse=True)
    else:
        my_tasks=UnitBasicInfo.objects.filter(areaCode=code).filter(inhouse=False)
    request_list = (my_tasks.filter(finished=True)
                    .order_by('-callTime'))
    return render(request, 'dispatcher/list.html', {'request':request_list})
def get_all_scheduled_records(request):
    code = request.session['user_code']
    my_tasks=""
    if code=="17":
        # my_tasks=UnitBasicInfo.objects.filter(
        #     Q(location_state='TX') | 
        #     Q(location_state='CA') |
        #     Q(location_state='LA') |
        #     Q(location_state='OK')).filter(inhouse=True)
        my_tasks=UnitBasicInfo.objects.filter(inhouse=True)
    elif code=="18":
        my_tasks=UnitBasicInfo.objects.filter(
            Q(location_state='MA') |
            Q(location_state='NJ') |
            Q(location_state='NH') |
            Q(location_state='CT') |
            Q(location_state='PA') |
            Q(location_state='VT') |
            Q(location_state='ME') |
            Q(location_state='RI') |
            Q(location_state='NY') |
            Q(location_state='DE')).filter(inhouse=True)
    else:
        my_tasks=UnitBasicInfo.objects.filter(areaCode=code).filter(inhouse=False)
    request_list = (my_tasks.filter(pre_diagnosis_flag=True)
                    .filter(finished=False)
                    .exclude(scheDate=None)
                    .order_by('scheDate'))
    return render(request, 'dispatcher/list.html', {'request':request_list})
def get_new_records(request):
    code = request.session['user_code']
    my_tasks=""
    if code=="17":
        # my_tasks=UnitBasicInfo.objects.filter(
        #     Q(location_state='TX') | 
        #     Q(location_state='CA') |
        #     Q(location_state='LA') |
        #     Q(location_state='OK')).filter(inhouse=True)
        my_tasks=UnitBasicInfo.objects.filter(inhouse=True)
    elif code=="18":
        my_tasks=UnitBasicInfo.objects.filter(
            Q(location_state='MA') |
            Q(location_state='NJ') |
            Q(location_state='NH') |
            Q(location_state='CT') |
            Q(location_state='PA') |
            Q(location_state='VT') |
            Q(location_state='ME') |
            Q(location_state='RI') |
            Q(location_state='NY') |
            Q(location_state='DE')).filter(inhouse=True)
    else:
        my_tasks=UnitBasicInfo.objects.filter(areaCode=code).filter(inhouse=False)
        print("-----")
    request_list = (my_tasks.filter(pre_diagnosis_flag=True)
                    .filter(warranty=True)
                    .filter(scheDate=None)
                    .filter(pre_diagnosis_pending=False)
                    .filter(long_term_pending=False)
                    .exclude(finished=True)
                    .order_by('-callTime'))
    for r in request_list:
        print (r)
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
    parts = PartRequest.objects.all().filter(sksid=unit.sksid)
    return render(request, 'dispatcher/followup.html', {'unit': unit,'parts':parts})
def show_service_detail(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    form=DispatchForm()
    return render(request, 'dispatcher/tech.html', {'unit': unit,'form':form})
def show_operator_page(request):
    if not request.session.get('is_login', None):
        return redirect("/user/login/")
    name=request.session['user_name']
    a=UnitBasicInfo.objects.all().filter(receiver=name).filter(callTime__gte=datetime.date.today()).count()
    b=UnitBasicInfo.objects.all().filter(receiver=name).filter(warranty=False).count()
    c=UnitBasicInfo.objects.all().filter(receiver=name).count()
    return render(request, 'operator/dashboard.html',{'today':a,'oow':b,'all':c})
def show_dispatcher_page(request):
    if not request.session.get('is_login', None):
        return redirect("/user/login/")
    name=request.session['user_name']
    code = request.session['user_code']
    user = Users.objects.get(code=code)
    my_tasks=UnitBasicInfo.objects.filter(areaCode=code).filter(inhouse=False)
    a=my_tasks.filter(warranty=True).filter(pre_diagnosis_flag=True).filter(pre_diagnosis_pending=False).filter(scheDate=None).exclude(finished=True).count()
    b=my_tasks.filter(finished=False).exclude(scheDate=None).count()
    c=my_tasks.filter(finished=True).count()
    d=PartRequest.objects.all().filter(code=code).count()
    return render(request, 'dispatcher/dashboard.html',{'new':a,'sche':b,'fin':c,'parts':d})
def show_inhouse_page(request):
    if not request.session.get('is_login', None):
        return redirect("/user/login/")
    name=request.session['user_name']
    code = request.session['user_code']
    tasks=""
    if code=="17":
        # tasks=UnitBasicInfo.objects.filter(
        #     Q(location_state='TX') | 
        #     Q(location_state='CA') |
        #     Q(location_state='LA') |
        #     Q(location_state='OK')).filter(inhouse=True)
        tasks=UnitBasicInfo.objects.filter(inhouse=True)
    elif code=="18":
        tasks=UnitBasicInfo.objects.filter(
            Q(location_state='MA') |
            Q(location_state='NJ') |
            Q(location_state='NH') |
            Q(location_state='CT') |
            Q(location_state='PA') |
            Q(location_state='VT') |
            Q(location_state='ME') |
            Q(location_state='RI') |
            Q(location_state='NY') |
            Q(location_state='DE')).filter(inhouse=True)
    a=(tasks.filter(scheDate=None)
        .exclude(finished=True)
        .count())
    b=(tasks.filter(finished=False)
        .exclude(scheDate=None)
        .count())
    c=tasks.filter(finished=True).count()
    d=PartRequest.objects.all().filter(code=code).count()
    return render(request, 'dispatcher/dashboard.html',{'new':a,'sche':b,'fin':c,'parts':d})
def show_admin_page(request):
    final_data = []
    final_data2 = []
    c1=0
    c2=0
    today = datetime.date.today()
    delta= datetime.timedelta(today.weekday())

    start = today-delta
    for user in OPERATOR_GROUP:
        count = UnitBasicInfo.objects.filter(receiver=user).filter(
            callTime__gte=start).count()
        final_data.append(count)
        c1=c1+count
    for code in [1,2,3,4,5,6]:
        count = Users.objects.get(code=code).current_tasks
        final_data2.append(count)
        c2=c2+count
    para = {
        'data':final_data,
        'data2':final_data2,
        'c1':c1,
        'c2':c2
    }
    return render(request, 'adm/dashboard.html', para)
@login_required(login_url='/user/login/')
def show_page(request):
    # if not request.session.get('is_login', None):
    #     return redirect("/user/login/")
    group = request.session['user_group']
    code = request.session['user_code']
    if group=="dispatcher":
        if (code == "17") or (code == "18"):
            return redirect('inhouse/')
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
    if group=="account":
        return redirect('/warranty/account/')
    return render(request, 'dispatcher/dashboard.html',{'new':a,'sche':b,'fin':c})
def user_login(request):
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
                username=user.name
                u = authenticate(request, username=username, password=password)
                # if user.password == password:
                #     request.session['is_login'] = True
                #     request.session['user_code'] = user.code
                #     request.session['user_name'] = user.name
                #     group=user.group
                #     request.session['user_group'] = group
                #     return redirect('/user/')
                # else:
                #     message = "Wrong password!"
                print(username,password)
                print(u)
                if u is not None:
                    login(request, u)
                    request.session['is_login'] = True
                    request.session['user_code'] = user.code
                    request.session['user_name'] = user.name
                    group=user.group
                    request.session['user_group'] = group
                    return redirect('/user/')
            except:
                message = "No such a user!"
    form=LoginForm()
    return render(request, 'request/login.html',{'form':form,'message':message})

def user_logout(request):
    logout(request)
    # if not request.session.get('is_login', None):
    #     return redirect("/user/login/")
    # request.session.flush()
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
