from curses.ascii import HT
from this import d
from django.shortcuts import redirect, render
from django.http import HttpResponse
from CookieSession import settings
import os
import datetime
# Create your views here.
def set_cookie_try(request,key=None,value=None):
    response = HttpResponse("Cookie 儲存完畢！")
    response.set_cookie(key,value)
    return response

def get_cookie_try(request,key=None):
    if key in request.COOKIES:
        return HttpResponse(f'{key} : {request.COOKIES[key]}')
    else:
        return HttpResponse('Cookie 不存在！')

def get_allcookies(request):
    if request.COOKIES != None:
        strcookies=''
        for key1, value1 in request.COOKIES.items():
            strcookies = strcookies + key1 + ":"+value1 +"<br>"
        return HttpResponse(strcookies)
    else:
        return HttpResponse('Cookie 不存在！')

def set_cookie2(request,key=None,value=None):
    response = HttpResponse("Cookie 有效時間為 1 小時！")
    response.set_cookie(key,value,max_age=3600)
    return response

def delete_cookie(request,key=None ):
    if key in request.COOKIES:
        response = HttpResponse('Delete Cookie: '+key)
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse(f"No cookies: {key}")

def navigate(request):
    return render(request,'navigate.html',locals())

def index(request):
    if "counter" in request.COOKIES:
        counter = int(request.COOKIES["counter"])
        counter += 1
    else:
        counter = 1
    dict1 = {"counter":counter}
    response = render(request,"index.html",locals())
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    tomorrow = datetime.datetime.replace(tomorrow,hour=0,minute=0,second=0)
    expires = datetime.datetime.strftime(tomorrow,"%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie("counter",counter,expires=expires)
    return response

def set_session(request,key=None,value=None):
    response = HttpResponse("Session 儲存完畢！")
    request.session[key]=value
    return response

def set_session2(request,key=None,value=None):
    response = HttpResponse("Session 儲存完畢！")
    request.session[key]=value
    request.session.set_expiry(30)
    return response
def get_session(request,key=None):
    if key in request.session:
        return HttpResponse(f"{key} : {request.session[key]}")
    else:
        return HttpResponse("Session 不存在！")

def get_allsessions(request):
    if request.session != None:
        strsessions = ''
        for key1, value1 in request.session.items():
            strsessions += strsessions + key1+" : "+str(value1)+"<br>"
        return HttpResponse(strsessions)
    else:
        return HttpResponse('Session 不存在！')

def delete_session(request,key=None):
    if key in request.session:
        response = HttpResponse(f"Delete Session: {key}")
        del request.session[key]
        return response
    else:
        return HttpResponse(f'No session: {key}')
def vote(request):
    if not "vote" in request.session:
        request.session["vote"]=True
        msg = "您第一次投票"
    else:
        msg = "您已投過票！"
    return HttpResponse(msg)

def login(request):
    username = "admin"
    password = "a123456"
    if request.method =="POST":
        if not 'username' in request.session:
            if request.POST['username']==username and request.POST['password']==password:
                request.session['username']=username
                message = username + " 您好，登入成功"
                status = "login"
    else:
        if 'username' in request.session:
            if request.session['username'] == username:
                message = request.session['username']+"您已登入過！"
                status = "login"
        else:
            message="帳號：admin 密碼：a123456 (請自行輸入)"
    return render(request,"login.html",locals())

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('/login/')