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

def v_eventf(request, *args, **kwargs):
 context={}
 return render(request,'user_register/v_event.html',context)

def acceptf (request, *args, **kwargs):
 context={}
 return render(request,'user_register/accept.html',context)
