from django.shortcuts import render
import random
# Create your views here.
def dice(request):
    no = random.randint(1,6)
    return render(request,"dice.html",{"no":no})

def dice2(request):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    no3 = random.randint(1,6)
    return render(request,"dice2.html",locals())

times = 0
def dice3(request):
    global times
    times += 1
    local_times = times
    username = "David"
    dict_no = {"no":random.randint(1,6)}
    return render(request,"dice3.html",locals())

def show(request):
    person1 = {"name":"Crystal","phone":"0912-234-234","age":20}
    person2 = {"name":"Mickey","phone":"0922-399-944","age":22}
    person3 = {"name":"Nancy","phone":"0953-254-662","age":25}
    persons = [person1,person2,person3]
    return render(request,"show.html",locals())

def filters(request):
    value = 4
    list1=[1,2,3]
    pw="芝麻開門"
    html="<span>Hello</span>"
    value2 = False
    return render(request,"filter.html",locals())