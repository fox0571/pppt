from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Users
# Create your views here.
def login(request):
    message=""
    if request.session.get('is_login',None):
        return redirect("/request/")
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            code = login_form.cleaned_data['user']
            password = login_form.cleaned_data['password']
            message = "hhhh"
            try:
                user = Users.objects.get(code=code)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_code'] = user.code
                    request.session['user_name'] = user.name
                    print (request.session['user_name'])
                    print(user.name)
                    return redirect('/request/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
    form=LoginForm()
    return render(request, 'request/login.html',{'form':form,'message':message})

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/request/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
