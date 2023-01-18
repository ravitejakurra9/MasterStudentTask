from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from MasterStudentApp.code import *
from MasterStudentApp.models import Master, Student, Task


# Create your views here.
def index_fun(request):
    return render(request,'index.html')


def masterlog_fun(request):
    if request.method=='POST':
        email = request.POST['txtemail']
        password = request.POST['txtpwd']
        if Master.objects.filter(Q(M_Email=email) & Q(M_Password=password)).exists():
            m = Master.objects.filter(M_Email=email)[0]
            return render(request,'navbar.html',{'m':m, 'mid':m.id})
        else:
            return render(request,'MasterLog.html',{'data':'Invalid user Name or Password'})


    return render(request,'MasterLog.html',{'data':''})


def masterreg_fun(request):

    if request.method=="POST":
        if Master.objects.filter(M_Email=request.POST['txtemail']).exists():
            return render(request, 'MasterReg.html',{'data':'Email already Exists Register With Other Email '})
        else:

            m = Master()
            m.M_Name=request.POST['txtname']
            m.M_Mobile=request.POST['txtmobile']
            m.M_Email=request.POST['txtemail']
            m.M_Password=request.POST['txtpwd']
            m.save()
            return redirect('mlog')
    return render(request,'MasterReg.html',{'data':''})


def studentlog_fun(request):
    if request.method=='POST':
        email = request.POST['txtemail']
        password = request.POST['txtpwd']
        if Student.objects.filter(Q(S_Email=email) & Q(S_Password=password)).exists():
            s = Student.objects.filter(Q(S_Email=email) & Q(S_Password=password))[0]
            return render(request, 'navbar1.html', {'sid': s.id, 's': s})
        else:
            return render(request, 'StudentLog.html', {"data": 'Invalid User Name Or Password',})

    return render(request,'StudentLog.html')

def studentreg_fun(request):

    if request.method=="POST":
        if Student.objects.filter(S_Email=request.POST['txtemail']).exists():
            return render(request, 'StudentReg.html',{'data':'Email already Exists Register With Other Email '})
        else:
            s = Student()
            s.S_Name=request.POST['txtname']
            s.S_Mobile=request.POST['txtmobile']
            s.S_Email=request.POST['txtemail']
            s.S_Password=request.POST['txtpwd']
            s.save()
            return redirect('slog')
    return render(request,'StudentReg.html',{'data':''})


def a_task_fun(request):
    s = Student.objects.all()
    if request.method=='POST':
        t = Task()
        t.Left = request.POST['ddlfno']
        t.Right = request.POST['ddlsno']
        t.Operation = request.POST['ddlop']
        t.Students = Student.objects.get(S_Name=request.POST['ddlstd'])
        t.Status = False
        t.save()
        return render(request,'task.html',{'note':'task Assigned Successfully To ','data':s,'name':request.POST['ddlstd']})
    return render(request,'task.html',{'data':s})

def viewalltask_fun(request):
    t = Task.objects.all()
    return render(request,'taskstatus.html',{'data':t})

def sp_fun(request,sid):
    t = Task.objects.filter(Q(Students_id=sid) & Q(Status=False))

    return render(request,'StdTask.html',{"data":t,'sid':sid})

def sc_fun(request,sid):
    t = Task.objects.filter(Q(Students_id=sid) & Q(Status=True))
    return render(request,'StdTask.html',{"data":t,'sid':sid})

def slove_fun(request,id):

    task = Task.objects.get(id=id)

    left = task.Left
    left = globals()[left]
    right = task.Right
    right = globals()[right]
    op = task.Operation
    op = globals()[op]
    res = left(op(right())) # it will go to code.py module where i kept the business logic
    task.Status=True
    task.save()
    s_id = task.Students_id
    s = Student.objects.get(id=s_id)
    t = Task.objects.filter(Q(Students_id=s.id) & Q(Status=False))
    taskdata = Task.objects.filter(id=id)

    return render(request, 'StdTask.html', {'data': t,'result':res,'sid':s.id,'task':taskdata})


def test_fun(request):
    return render(request,'test.html')


def std_home_fun(request,sid):
    s = Student.objects.get(id=sid)
    return render(request, 'navbar1.html', {'sid': s.id, 's': s})