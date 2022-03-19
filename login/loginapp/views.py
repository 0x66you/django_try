from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
# Create your views here.
def adduser(request):
    try:
        user = User.objects.get(username="test")
    except:
        user = None
    if user != None:
        message = user.username + " 帳號已建立！"
        return HttpResponse(message)
    else:
        user = User.objects.create_user("test","test@test.com.tw","a123456!")
        user.first_name="郁庭"
        user.last_name="簡"
        user.is_staff = True
        user.save()
        return redirect('/admin/')

def index(request):
    return render(request,'index.html',locals())

def login(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"] 
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                message = '登入成功'
                return render(request,'index.html',locals())
            else:
                message = "帳號尚未啟用！"
        else:
            message = "登入失敗！"
    return render(request,'login.html',locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')