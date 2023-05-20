from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from school_system_app.models import CustomUser, Courses, SessionYearModel, Subjects, Stages


def admin_home(request):
    return render(request, "hod_templates/home_content.html")



def add_staff(request):
    return render(request,"hod_templates/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            address=request.POST.get("address")
            puk=request.POST.get("puk")
            contact=request.POST.get("contact")
            bank_name=request.POST.get("bank_name")
            bank_account=request.POST.get("bank_account")
            salary=request.POST.get("salary")
            allowance=request.POST.get("allowance")
            ezwich=request.POST.get("ezwich")
            momo_number=request.POST.get("momo_number")

            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                user.staff.address=address
                user.staff.puk=puk
                user.staff.contact=contact
                user.staff.bank_name=bank_name
                user.staff.bank_account=bank_account
                user.staff.salary=salary
                user.staff.allowance=allowance
                user.staff.ezwich=ezwich
                user.staff.momo_number=momo_number
                user.staff.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Staff")
                return HttpResponseRedirect(reverse("add_staff"))
            except:
                messages.error(request,"Failed to Add staff")
                return HttpResponseRedirect(reverse("add_staff"))
            
            
def add_employee(request):
    return render(request,"hod_templates/add_employee_template.html")


def add_employee_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            address=request.POST.get("address")
            puk=request.POST.get("puk")
            qualification=request.POST.get("qualification")
            role=request.POST.get("role")
            department=request.POST.get("department")
            contact=request.POST.get("contact")
            bank_name=request.POST.get("bank_name")
            bank_account=request.POST.get("bank_account")
            salary=request.POST.get("salary")
            allowance=request.POST.get("allowance")
            ezwich=request.POST.get("ezwich")
            momo_number=request.POST.get("momo_number")

            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=6)
                user.employee.address=address
                user.employee.puk=puk
                user.employee.qualification=qualification
                user.employee.role=role
                user.employee.department=department
                user.employee.contact=contact
                user.employee.bank_name=bank_name
                user.employee.bank_account=bank_account
                user.employee.salary=salary
                user.employee.allowance=allowance
                user.employee.ezwich=ezwich
                user.employee.momo_number=momo_number
                user.employee.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Employee")
                return HttpResponseRedirect(reverse("add_employee"))
            except:
                messages.error(request,"Failed to Add Employee")
                return HttpResponseRedirect(reverse("add_employee"))


def add_accounts(request):
    return render(request,"hod_templates/add_accounts_template.html")

def add_accounts_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
            first_name=request.POST.get("first_name")
            last_name=request.POST.get("last_name")
            username=request.POST.get("username")
            email=request.POST.get("email")
            password=request.POST.get("password")
            address=request.POST.get("address")
            puk=request.POST.get("puk")
            contact=request.POST.get("contact")
            #bank_name=request.POST.get("bank_name")
            #bank_account=request.POST.get("bank_account")
            #salary=request.POST.get("salary")
            #allowance=request.POST.get("allowance")
            #ezwich=request.POST.get("ezwich")
            #momo_number=request.POST.get("momo_number")

            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)

            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=5)
                user.accounts.address=address
                user.accounts.puk=puk
                user.accounts.contact=contact
                #user.staff.bank_name=bank_name
                #user.staff.bank_account=bank_account
                #user.staff.salary=salary
                #user.staff.allowance=allowance
                #user.staff.ezwich=ezwich
                #user.staff.momo_number=momo_number
                user.accounts.profile_pic=profile_pic_url
                user.save()
                messages.success(request,"Successfully Added Accountant")
                return HttpResponseRedirect(reverse("add_accounts"))
            except:
                messages.error(request,"Failed to Add Accountant")
                return HttpResponseRedirect(reverse("add_accounts"))


def add_session(request):
    return render(request,"hod_templates/add_session_template.html")

def add_session_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
            semester_name=request.POST.get("semester_name")
            session_start_year=request.POST.get("session_start_year")
            session_end_year=request.POST.get("session_end_year")

            try:
                session_model=SessionYearModel(semester_name=semester_name,session_start_year=session_start_year,session_end_year=session_end_year)
                session_model.save()
                messages.success(request,"Successfully Added Session")
                return HttpResponseRedirect(reverse("add_session"))
            except:
                messages.error(request,"Failed to Add Session")
                return HttpResponseRedirect(reverse("add_session"))


def add_course(request):
    return render(request,"hod_templates/add_course_template.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        puk=request.POST.get("puk")
        course_name=request.POST.get("course_name")

        try:
            course_model=Courses(course_name=course_name, puk=puk)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("add_course"))
        except Exception as e:
            print(e)
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect(reverse("add_course"))


def add_subject(request):
    courses=Courses.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_templates/add_subject_template.html",{"staffs":staffs,"courses":courses})

def add_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        puk=request.POST.get("puk")
        subject_name=request.POST.get("subject_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Subjects(puk=puk,subject_name=subject_name,course_id=course,staff_id=staff)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return HttpResponseRedirect(reverse("add_subject"))
        except:
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))


def add_stage(request):
    courses=Courses.objects.all()
    subjects=Subjects.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_templates/add_stage_template.html",{"staffs":staffs,"courses":courses,"subjects":subjects})

def add_stage_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        stage_name=request.POST.get("stage_name")
        course_id=request.POST.get("course")
        course=Courses.objects.get(id=course_id)
        subject_id=request.POST.get("subject")
        subject=Subjects.objects.get(id=subject_id)
        staff_id=request.POST.get("staff")
        staff=CustomUser.objects.get(id=staff_id)

        try:
            subject=Stages(stage_name=stage_name,course_id=course,staff_id=staff,subject_id=subject)
            subject.save()
            messages.success(request,"Successfully Added Class")
            return HttpResponseRedirect(reverse("add_stage"))
        except:
            messages.error(request,"Failed to Add Class")
            return HttpResponseRedirect(reverse("add_stage"))


def add_student(request):
    courses=Courses.objects.all()
    subjects=Subjects.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request, "hod_templates/add_student_template.html",{"staffs":staffs,"courses":courses,"subjects":subjects})


def add_student_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        admission_number = request.POST.get("admission_number")
        qualification = request.POST.get("qualification")
        role = request.POST.get("role")
        department = request.POST.get("department")
        contact = request.POST.get("contact")
        bank_name = request.POST.get("bank_name")
        bank_account = request.POST.get("bank_account")
        salary = request.POST.get("salary")
        allowance = request.POST.get("allowance")
        ezwich = request.POST.get("ezwich")
        momo_number = request.POST.get("momo_number")

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.employee.address = address
            user.employee.admission_number = admission_number
            user.employee.qualification = qualification
            user.employee.role = role
            user.employee.department = department
            user.employee.contact = contact
            user.employee.bank_name = bank_name
            user.employee.bank_account = bank_account
            user.employee.salary = salary
            user.employee.allowance = allowance
            user.employee.ezwich = ezwich
            user.employee.momo_number = momo_number
            user.employee.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully Added Employee")
            return HttpResponseRedirect(reverse("add_employee"))
        except:
            messages.error(request, "Failed to Add Employee")
            return HttpResponseRedirect(reverse("add_employee"))