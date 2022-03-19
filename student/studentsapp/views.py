from django.shortcuts import redirect, render
from studentsapp.models import student
from studentsapp.form import PostForm
# Create your views here.

def index(request):
    students = student.objects.all().order_by('id')
    return render(request,"index.html",locals())

def listone(request):
    try:
        unit = student.objects.get(cName="林宣霓") #讀取一筆資料
    except:
        errormessage = "(讀取錯誤！)"
    return render(request,'listone.html',locals())

def listall(request):
    students = student.objects.all().order_by('id')
    return render(request,"listall.html",locals())

def post(request):
    if request.method =="POST":
        mess = request.POST['username']
    else:
        mess = "表單資料尚未送出！"
    return render(request,'post.html',locals())

def post1(request):
    if request.method == "POST":
        cName = request.POST['cName']
        cSex = request.POST['cSex']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']
        # 新增一筆資料
        unit = student.objects.create(cName = cName, cSex = cSex,
                                      cBirthday=cBirthday, cEmail = cEmail,
                                      cPhone = cPhone, cAddr = cAddr)
        unit.save()
        return redirect('/')
    else:
        message = '請輸入資料(資料不做驗證)'
    return render(request,'post1.html',locals())

def postform(request):
    postform = PostForm()
    return render(request,"postform.html",locals())

def post2(request):
    if request.method == "POST":
        postform = PostForm(request.POST)
        if postform.is_valid():
            cName = postform.cleaned_data['cName']
            cSex = postform.cleaned_data['cSex']
            cBirthday = postform.cleaned_data['cBirthday']
            cEmail = postform.cleaned_data['cEmail']
            cPhone = postform.cleaned_data['cPhone']
            cAddr = postform.cleaned_data['cAddr']
            # 新增一筆資料
            unit = student.objects.create(cName = cName, cSex = cSex,
                                      cBirthday=cBirthday, cEmail = cEmail,
                                      cPhone = cPhone, cAddr = cAddr)
            unit.save()
            return redirect('/')
        else:
            message = "驗證碼錯誤！"
    else:
        message="姓名、性別、生日必須輸入"
        postform = PostForm() # 產生表單用
    return render(request,"post2.html",locals())

def delete(request,id=None):
    if id != None:
        if request.method == "POST":
            id = request.POST["cId"]
        try:
            unit = student.objects.get(id=id)
            unit.delete()
            return redirect('/')
        except:
            message = "讀取錯誤！"
    return render(request,"delete.html",locals())

def edit(request,id=None,mode=None):
    if mode == "edit":
        unit = student.objects.get(id=id)
        unit.cName = request.GET["cName"]
        unit.cSex = request.GET["cSex"]
        unit.cBirthday = request.GET["cBirthday"]
        unit.cEmail = request.GET["cEmail"]
        unit.cPhone = request.GET["cPhone"]
        unit.cAddr = request.GET["cAddr"]
        unit.save()
        message = '已修改..'
        return redirect('/')
    else:
        try:
            unit = student.objects.get(id=id)
            strdate = str(unit.cBirthday)\
                        .replace("年","-")\
                        .replace("月","-")\
                        .replace("日","-")
            unit.cBirthday = strdate
        except:
            message = "此 id 不存在！"
    return render(request,'edit.html',locals())

def edit2(request,id=None,mode=None):
    if mode == "load":
        unit = student.objects.get(id=id)
        strdate = str(unit.cBirthday).replace("年","-").replace("月","-").replace("日","-")
        unit.cBirthday = strdate
        return render(request,"edit2.html",locals())
    elif mode == "save":
        unit = student.objects.get(id=id)
        unit.cName = request.GET["cName"]
        unit.cSex = request.GET["cSex"]
        unit.cBirthday = request.GET["cBirthday"]
        unit.cEmail = request.GET["cEmail"]
        unit.cPhone = request.GET["cPhone"]
        unit.cAddr = request.GET["cAddr"]
        unit.save()
        return redirect("/")