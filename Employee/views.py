from django.shortcuts import render,redirect
from .models import Emp
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def emp_home(request):
    print("Home page is called.")
    emps=Emp.objects.all()
    return render(request,"home.html",{
        'emps':emps
    })
def index(request):
    print("index page is called.")
    emps=Emp.objects.all()
    return render(request,"index.html",{
        'emps':emps
    })



def emp_add(request):
    print("emp add page is called.")
    if request.method=='POST':

        # Data is fetch
        emp_id=request.POST.get("emp_id")
        emp_name=request.POST.get("emp_name")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_department=request.POST.get("emp_department")
        emp_working=request.POST.get("emp_working")

        # Backend validation
        if not all([emp_id, emp_name, emp_phone, emp_address, emp_department]):
            return render(request, 'emp_add.html', {'error': 'Complete fill the form.'})

        # Create model object and set the data.
        e=Emp()
        e.emp_id=emp_id
        e.name=emp_name
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        # Save object
        e.save()
        print("Data is coming!")
        return redirect("/home/")
    return render(request,"emp_add.html",{})



def delete_emp(request,emp_id):
    print(emp_id)
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect('/home/')

def update_emp(request,emp_id):

    emp=Emp.objects.get(pk=emp_id)
    print("update emp called!")
    print(emp_id)
    return render(request,"update_emp.html",{
        'emp':emp
    })




def do_update_emp(request,emp_id):
    print("Called! do update emp")
    if request.method == 'POST':
        # Data is fetch
        emp_id_tem = request.POST.get("emp_id")
        emp_name = request.POST.get("emp_name")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_department = request.POST.get("emp_department")
        emp_working = request.POST.get("emp_working")
        # Backend validation

        # Create model object and set the data.
        e=Emp.objects.get(pk=emp_id)
        e.emp_id = emp_id_tem
        e.name = emp_name
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        # Save object
        e.save()
    return redirect("/home/")

