from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from students.models import Student, Register,Staff
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import pdb


def main(request):
    return render(request, 'students/main.html')


def application(request):
    return render(request, 'students/application.html')


def save(request):
    Student.objects.create(student_name=request.POST['name'], student_email=request.POST['email'],
                           student_phone=request.POST['phone'], ssc_marks=request.POST['ssc_marks'],
                           inter_marks=request.POST['inter_marks'])
    return HttpResponseRedirect('/students/')


def registration(request):
    return render(request, 'students/register.html')


def save_details(request):
    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    student = Student.objects.get(student_email=request.POST["email"])
    Register.objects.create(department=request.POST['department'], user=user, Student=student)
    return HttpResponseRedirect('/students/')


def login_info(request):
    return render(request, 'students/login.html')


def validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/students/details/')
    else:
        return HttpResponse("invalid username or password")


def details(request):

    #pdb.set_trace()
    user = request.user
    #student = Student.objects.get(student_email=request.POST["email"])
    return render(request, 'students/details.html', {'user': user})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/students/login/')


def staff_registration(request):
    return render(request, 'students/staff.html')


def save_staffdetails(request):
    user=User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    Staff.objects.create(staff_name=request.POST['name'], staff_email=request.POST['email'],
                         staff_phone=request.POST['phone'], qualification=request.POST['qualification'],
                         staff_department=request.POST['department'],
                         experiance=request.POST['experiance'],user=user)

    return HttpResponseRedirect('/students/')


def staff_validate(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/students/staff_details/')
    else:
        return HttpResponse("invalid username or password")


def staff_login(request):
    return render(request,'students/staff_login.html')

def staff_detail(request):
   # pdb.set_trace()
    user = request.user
    return render(request,'students/staff_details.html',{'user':user})

def staff_logout(request):
    logout(request)
    return HttpResponseRedirect('/students/staff_login/')

def total_staff(request):
    pdb.set_trace()
    staff=Staff.objects.all()
    return render(request,'students/totalstaff.html',{'staff':staff})