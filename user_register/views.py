# Create your views here.
from django.shortcuts import render,redirect
# from .forms import *
from .models import *
def employee_list(request):
    # employeel = list()
    employeel = list(Employee.objects.values('eno', 'ename', 'mobile', 'position_id'))
    # for i in range(len(Employee.objects.all())):
    #     print("i")
    #     employeel.append(employeeobj[i])
    context = {'employeel':employeel}
    print(len(context['employeel']))
    print(context)
    return render(request,"user_register/employee_list.html",context)


def homepagef(request, *args, **kwargs):
 context={}
 return render(request,'user_register/homepage.html',context)

def charityregisterf(request, *args, **kwargs):
 context={}
 b1 = request.GET.get('b1')
 b2 = request.GET.get('b2')
 if details.objects.filter(uid=b1).count()==0:
     print("not found")
 return render(request,'user_register/charityregister.html',context)

def event_regf(request, *args, **kwargs):
 context={}
 return render(request,'user_register/event_reg.html',context)

def event_addf(request, *args, **kwargs):
 context={}
 b1 = request.GET.get('edate')
 b2 = request.GET.get('etime')
 b3 = request.GET.get('eloc')
 evnts.objects.create(edate=b1,etime=b2,eloct=b3)
 return render(request,'user_register/event_reg.html',context)

def v_eventf(request, *args, **kwargs):
 context={}
 b1 = request.GET.get('uid')
 b2 = request.GET.get('pwd')
 evntsl = list(evnts.objects.values('edate', 'etime', 'eloct'))
 context = {'evntsl':evntsl}
 print(len(context['evntsl']))
 print(context)
 return render(request,'user_register/v_event.html',context)

def addc (request, *args, **kwargs):
 context={}
 b1 = request.GET.get('uid')
 b2 = request.GET.get('pwd')
 b3 = request.GET.get('emailid')
 details.objects.create(utype='c',uid=b1,pwd=b2,email=b3)

 return render(request,'user_register/homepage.html',context)

def addv (request, *args, **kwargs):
 b1 = request.GET.get('uid')
 b2 = request.GET.get('pwd')
 b3 = request.GET.get('emailid')
 details.objects.create(utype='v',uid=b1,pwd=b2,email=b3)
 context={}
 return render(request,'user_register/homepage.html',context)


