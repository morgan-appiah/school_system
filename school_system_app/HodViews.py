from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from school_system_app.models import CustomUser, Courses, SessionYearModel, Subjects, Stages, Staff, Employee, Parent, \
    Student, Accounts


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
    stages=Stages.objects.all()
    session_years=SessionYearModel.objects.all()
    staffs=CustomUser.objects.filter(user_type=2)
    return render(request, "hod_templates/add_student_template.html",{"staffs":staffs,"courses":courses,"stages":stages,"session_years":session_years})


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
        contact = request.POST.get("contact")
        admission_date = request.POST.get("admission_date")
        religion = request.POST.get("religion")
        mother = request.POST.get("mother")
        father = request.POST.get("father")
        guardian_name = request.POST.get("guardian_name")
        guardian_relationship = request.POST.get("guardian_relationship")
        gender = request.POST.get("gender")
        emergency_contact = request.POST.get("emergency_contact")
        nonclass_activity = request.POST.get("nonclass_activity")
        previous_health = request.POST.get("previous_health")
        previous_school = request.POST.get("previous_school")
        dob = request.POST.get("dob")
        nationality = request.POST.get("nationality")
        hometown = request.POST.get("hometown")
        gps_address = request.POST.get("gps_address")
        category = request.POST.get("category")
        alt_email = request.POST.get("alt_email")
        hostel = request.POST.get("hostel")
        course_id = request.POST.get("course")
        course = Courses.objects.get(id=course_id)
        academic_tutor = request.POST.get("staff")
        staff = CustomUser.objects.get(id=academic_tutor)
        stage_id = request.POST.get("stage")
        stage = Stages.objects.get(id=stage_id)

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=3)
            user.student.address = address
            user.student.admission_number = admission_number
            user.student.admission_date = admission_date
            user.student.religion = religion
            user.student.mother = mother
            user.student.contact = contact
            user.student.father = father
            user.student.guardian_name = guardian_name
            user.student.guardian_relationship = guardian_relationship
            user.student.gps_address = gps_address
            user.student.gender = gender
            user.student.hometown = hometown
            user.student.hostel = hostel
            user.student.nationality = nationality
            user.student.nonclass_activity = nonclass_activity
            user.student.previous_health = previous_health
            user.student.previous_school = previous_school
            user.student.dob = dob
            user.student.category = category
            user.student.emergency_contact = emergency_contact
            user.student.alt_email = alt_email
            user.student.course = course
            user.student.stage = stage
            user.student.staff = staff
            user.student.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request, "Failed to Add Student")
            return HttpResponseRedirect(reverse("add_student"))
        
        
def add_parent(request):
    staffs=CustomUser.objects.filter(user_type=2)
    students=CustomUser.objects.filter(user_type=3)
    return render(request, "hod_templates/add_parent_template.html",{"staffs":staffs,"students":students})


def add_parent_save(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        puk = request.POST.get("puk")
        contact = request.POST.get("contact")
        tutor_contact = request.POST.get("tutor_contact")
        occupation = request.POST.get("occupation")
        ward = request.POST.get("student")
        student = CustomUser.objects.get(id=ward)
        ward_tutor = request.POST.get("staff")
        staff = CustomUser.objects.get(id=ward_tutor)

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email,
                                                  last_name=last_name, first_name=first_name, user_type=4)
            user.parent.address = address
            user.parent.puk = puk
            user.parent.tutor_contact = tutor_contact
            user.parent.occupation = occupation
            user.parent.contact = contact
            user.parent.student = student
            user.parent.staff = staff
            user.parent.profile_pic = profile_pic_url
            user.save()
            messages.success(request, "Successfully Added Parent")
            return HttpResponseRedirect(reverse("add_parent"))
        except:
            messages.error(request, "Failed to Add Parent")
            return HttpResponseRedirect(reverse("add_parent"))


def manage_staff(request):
    staffs=Staff.objects.all()
    return render(request,"hod_templates/manage_staff_template.html",{"staffs":staffs})


def staff_profile(request, staff_id):
    staff = Staff.objects.get(admin=staff_id)
    return render(request, "hod_templates/staff_profile_template.html", {"staff": staff, "id": staff_id})


def edit_staff(request, staff_id):
    staff=Staff.objects.get(admin=staff_id)
    return render(request,"hod_templates/edit_staff_template.html",{"staff":staff,"id":staff_id})


def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        puk = request.POST.get("puk")
        contact = request.POST.get("contact")
        bank_name = request.POST.get("bank_name")
        bank_account = request.POST.get("bank_account")
        salary = request.POST.get("salary")
        allowance = request.POST.get("allowance")
        ezwich = request.POST.get("ezwich")
        momo_number = request.POST.get("momo_number")

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=staff_id)
            user.username=username
            user.password=password
            user.email=email
            user.last_name=last_name
            user.first_name=first_name
            user.save()

            staff_model = Staff.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.puk = puk
            staff_model.contact = contact
            staff_model.bank_name = bank_name
            staff_model.bank_account = bank_account
            staff_model.salary = salary
            staff_model.allowance = allowance
            staff_model.ezwich = ezwich
            staff_model.momo_number = momo_number

            if profile_pic_url != None:
                staff_model.profile_pic = profile_pic_url

            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("edit_staff",kwargs={"staff_id":staff_id}))




def manage_employee(request):
    employees=Employee.objects.all()
    return render(request,"hod_templates/manage_employee_template.html",{"employees":employees})


def employee_profile(request, employee_id):
    employee = Employee.objects.get(admin=employee_id)
    return render(request, "hod_templates/employee_profile_template.html", {"employee": employee, "id": employee_id})


def edit_employee(request, employee_id):
    employee = Employee.objects.get(admin=employee_id)
    return render(request, "hod_templates/edit_employee_template.html", {"employee": employee, "id": employee_id})


def edit_employee_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        employee_id=request.POST.get("employee_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        puk = request.POST.get("puk")
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

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=employee_id)
            user.username=username
            user.password=password
            user.email=email
            user.last_name=last_name
            user.first_name=first_name
            user.save()

            employee_model = Staff.objects.get(admin=employee_id)
            employee_model.address = address
            employee_model.puk = puk
            employee_model.qualification = qualification
            employee_model.role = role
            employee_model.department = department
            employee_model.contact = contact
            employee_model.bank_name = bank_name
            employee_model.bank_account = bank_account
            employee_model.salary = salary
            employee_model.allowance = allowance
            employee_model.ezwich = ezwich
            employee_model.momo_number = momo_number

            if profile_pic_url != None:
                employee_model.profile_pic = profile_pic_url

            employee_model.save()
            messages.success(request,"Successfully Edited Employee")
            return HttpResponseRedirect(reverse("edit_employee",kwargs={"employee_id":employee_id}))
        except:
            messages.error(request,"Failed to Edit Employee")
            return HttpResponseRedirect(reverse("edit_employee",kwargs={"employee_id":employee_id}))



def manage_parent(request):
    parents=Parent.objects.all()
    return render(request,"hod_templates/manage_parent_template.html",{"parents":parents})


def parent_profile(request, parent_id):
    parent = Parent.objects.get(admin=parent_id)
    staff=CustomUser.objects.filter(user_type=2)
    student=CustomUser.objects.filter(user_type=3)
    return render(request, "hod_templates/parent_profile_template.html", {"parent": parent, "id": parent_id, "staff":staff, "student":student})


def edit_parent(request, parent_id):
    parent = Parent.objects.get(admin=parent_id)
    return render(request, "hod_templates/edit_parent_template.html", {"parent": parent, "id": parent_id})


def edit_parent_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        parent_id=request.POST.get("parent_id")
        staff_id=request.POST.get("staff")
        student_id=request.POST.get("student")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        puk = request.POST.get("puk")
        contact = request.POST.get("contact")
        tutor_contact = request.POST.get("tutor_contact")
        occupation = request.POST.get("occupation")

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        #try:
        user = CustomUser.objects.get(id=parent_id)
        user.username=username
        user.password=password
        user.email=email
        user.last_name=last_name
        user.first_name=first_name
        user.save()
        parent_model = Parent.objects.get(admin=parent_id)
        parent_model.address = address
        parent_model.puk = puk
        parent_model.tutor_contact = tutor_contact
        parent_model.occupation = occupation
        student = Student.objects.get(id=student_id)
        parent_model.student_id = student
        parent_model.contact = contact
        staff = Staff.objects.get(id=staff_id)
        parent_model.staff_id = staff
        if profile_pic_url != None:
            parent_model.profile_pic = profile_pic_url
        parent_model.save()
        messages.success(request,"Successfully Edited Parent")
        return HttpResponseRedirect(reverse("edit_parent",kwargs={"parent_id":parent_id}))
        #except:
        #    messages.error(request,"Failed to Edit Parent")
        #    return HttpResponseRedirect(reverse("edit_parent",kwargs={"parent_id":parent_id}))



def manage_accounts(request):
    accounts=Accounts.objects.all()
    return render(request,"hod_templates/manage_accounts_template.html",{"accounts":accounts})


def accounts_profile(request, accounts_id):
    account = Accounts.objects.get(admin=accounts_id)
    return render(request, "hod_templates/accounts_profile_template.html", {"account": account, "id": accounts_id})


def edit_accounts(request, accounts_id):
    account = Accounts.objects.get(admin=accounts_id)
    return render(request, "hod_templates/edit_accounts_template.html", {"account": account, "id": accounts_id})


def edit_accounts_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        accounts_id=request.POST.get("accounts_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        puk = request.POST.get("puk")
        contact = request.POST.get("contact")

     

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=accounts_id)
            user.username=username
            user.password=password
            user.email=email
            user.last_name=last_name
            user.first_name=first_name
            user.save()

            accounts_model = Staff.objects.get(admin=accounts_id)
            accounts_model.address = address
            accounts_model.puk = puk
            accounts_model.contact = contact
       

            if profile_pic_url != None:
                accounts_model.profile_pic = profile_pic_url

            accounts_model.save()
            messages.success(request,"Successfully Edited Accountant")
            return HttpResponseRedirect(reverse("edit_accounts",kwargs={"accounts_id":accounts_id}))
        except:
            messages.error(request,"Failed to Edit Accountant")
            return HttpResponseRedirect(reverse("edit_accounts",kwargs={"accounts_id":accounts_id}))


def manage_student(request):
    students=Student.objects.all()
    return render(request,"hod_templates/manage_student_template.html",{"students":students})


def student_profile(request, student_id):
    student = Student.objects.get(admin=student_id)
    courses = Courses.objects.all()
    stage = Stages.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, "hod_templates/student_profile_template.html", {"student":student, "id":student_id,"staffs":staffs,"courses":courses,"stage":stage})


def edit_student(request, student_id):
    student=Student.objects.get(admin=student_id)
    return render(request, "hod_templates/edit_student_template.html", {"student":student, "id":student_id})


def edit_student_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        student_id=request.POST.get("student_id")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        admission_number = request.POST.get("admission_number")
        contact = request.POST.get("contact")
        admission_date = request.POST.get("admission_date")
        religion = request.POST.get("religion")
        mother = request.POST.get("mother")
        father = request.POST.get("father")
        guardian_name = request.POST.get("guardian_name")
        guardian_relationship = request.POST.get("guardian_relationship")
        gender = request.POST.get("gender")
        emergency_contact = request.POST.get("emergency_contact")
        nonclass_activity = request.POST.get("nonclass_activity")
        previous_health = request.POST.get("previous_health")
        previous_school = request.POST.get("previous_school")
        dob = request.POST.get("dob")
        nationality = request.POST.get("nationality")
        hometown = request.POST.get("hometown")
        gps_address = request.POST.get("gps_address")
        category = request.POST.get("category")
        alt_email = request.POST.get("alt_email")
        hostel = request.POST.get("hostel")
        staff_id = request.POST.get("staff")
        course_id = request.POST.get("course")
        stage_id = request.POST.get("stage")

        if request.FILES.get('profile_pic', False):
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)
        else:
            profile_pic_url = None

        try:
            user = CustomUser.objects.get(id=student_id)
            user.username=username
            user.password=password
            user.email=email
            user.last_name=last_name
            user.first_name=first_name
            user.save()

            student_model = Student.objects.get(admin=student_id)
            student_model.address = address
            student_model.admission_number = admission_number
            student_model.contact = contact
            student_model.admission_date = admission_date
            student_model.religion = religion
            student_model.mother = mother
            student_model.father = father
            student_model.guardian_name = guardian_name
            student_model.guardian_relationship = guardian_relationship
            student_model.gender = gender
            student_model.emergency_contact = emergency_contact
            student_model.nonclass_activity = nonclass_activity
            student_model.previous_health = previous_health
            student_model.previous_school = previous_school
            student_model.dob = dob
            student_model.nationality = nationality
            student_model.hometown = hometown
            student_model.gps_address = gps_address
            student_model.category = category
            student_model.alt_email = alt_email
            student_model.hostel = hostel
            staff = CustomUser.objects.get(id=staff_id)
            student_model.staff_id = staff
            course = Courses.objects.get(id=course_id)
            student_model.course_id = course
            stage = Stages.objects.get(id=stage_id)
            student_model.stage_id = stage

            if profile_pic_url != None:
                student_model.profile_pic = profile_pic_url

            student_model.save()
            messages.success(request,"Successfully Edited Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))
        except:
            messages.error(request,"Failed to Edit Student")
            return HttpResponseRedirect(reverse("edit_student",kwargs={"student_id":student_id}))


def manage_session(request):
    sessions=SessionYearModel.objects.all()
    return render(request,"hod_templates/manage_session_template.html",{"sessions":sessions})


def edit_session(request,session_id):
    session=SessionYearModel.objects.get(id=session_id)
    return render(request,"hod_templates/edit_session_template.html",{"session":session,"id":session_id})

def edit_session_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        session_id=request.POST.get("session_id")
        semester_name = request.POST.get("semester_name")
        session_start_year = request.POST.get("session_start_year")
        session_end_year = request.POST.get("session_end_year")

        try:
            session=SessionYearModel.objects.get(id=session_id)
            print(SessionYearModel.semester_name)
            session.semester_name=semester_name
            session.session_start_year=session_start_year
            session.session_end_year=session_end_year
            session.save()
            messages.success(request,"Successfully Edited Session Year")
            return HttpResponseRedirect(reverse("edit_session",kwargs={"session_id":session_id}))
        except:
            messages.error(request,"Failed to Edit Session Year")
            return HttpResponseRedirect(reverse("edit_session",kwargs={"session_id":session_id}))


def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"hod_templates/manage_course_template.html",{"courses":courses})


def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"hod_templates/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        puk = request.POST.get("puk")
        course_name = request.POST.get("course_name")

        try:
            course=Courses.objects.get(id=course_id)
            print(Courses.course_name)
            course.puk=puk
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))
        except:
            messages.error(request,"Failed to Edit Course")
            return HttpResponseRedirect(reverse("edit_course",kwargs={"course_id":course_id}))


def manage_subject(request):
    subjects=Subjects.objects.all()
    return render(request,"hod_templates/manage_subject_template.html",{"subjects":subjects})

def edit_subject(request,subject_id):
    subject=Subjects.objects.get(id=subject_id)
    courses=Courses.objects.all()
    staff=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_templates/edit_subject_template.html",{"subject":subject,"staff":staff,"courses":courses,"id":subject_id})

def edit_subject_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subject_id=request.POST.get("subject_id")
        puk=request.POST.get("puk")
        subject_name=request.POST.get("subject_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            subject=Subjects.objects.get(id=subject_id)
            subject.puk=puk
            subject.subject_name=subject_name
            staff=CustomUser.objects.get(id=staff_id)
            subject.staff_id=staff
            course=Courses.objects.get(id=course_id)
            subject.course_id=course
            subject.save()

            messages.success(request,"Successfully Edited Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))
        except:
            messages.error(request,"Failed to Edit Subject")
            return HttpResponseRedirect(reverse("edit_subject",kwargs={"subject_id":subject_id}))


def manage_stage(request):
    stages=Stages.objects.all()
    return render(request,"hod_templates/manage_stage_template.html",{"stages":stages})

def edit_stage(request,stage_id):
    stage=Stages.objects.get(id=stage_id)
    courses=Courses.objects.all()
    staff=CustomUser.objects.filter(user_type=2)
    return render(request,"hod_templates/edit_subject_template.html",{"stage":stage,"staff":staff,"courses":courses,"id":stage_id})

def edit_stage_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        stage_id=request.POST.get("stage_id")
        stage_name=request.POST.get("stage_name")
        staff_id=request.POST.get("staff")
        course_id=request.POST.get("course")

        try:
            stage=Stages.objects.get(id=stage_id)
            stage.stage_name=stage_name
            staff=CustomUser.objects.get(id=staff_id)
            stage.staff_id=staff
            course=Courses.objects.get(id=course_id)
            stage.course_id=course
            stage.save()

            messages.success(request,"Successfully Edited Class")
            return HttpResponseRedirect(reverse("edit_stage",kwargs={"stage_id":stage_id}))
        except:
            messages.error(request,"Failed to Edit Stage")
            return HttpResponseRedirect(reverse("edit_stage",kwargs={"stage_id":stage_id}))


def delete_staff(request, staff_id):
    staff = Staff.objects.get(admin=staff_id)
    try:
        staff.delete()
        messages.success(request, "Staff Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_staff"))
    except:
        messages.error(request, "Failed To Delete Staff")
        return HttpResponseRedirect(reverse("manage_staff"))


def delete_employee(request, employee_id):
    employee = Employee.objects.get(admin=employee_id)
    try:
        employee.delete()
        messages.success(request, "Employee Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_employee"))
    except:
        messages.error(request, "Failed To Delete Employee")
        return HttpResponseRedirect(reverse("manage_employee"))
    
      
def delete_parent(request, parent_id):
    parent = Parent.objects.get(admin=parent_id)
    try:
        parent.delete()
        messages.success(request, "Parent Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_parent"))
    except:
        messages.error(request, "Failed To Delete Parent")
        return HttpResponseRedirect(reverse("manage_parent"))


def delete_accounts(request, accounts_id):
    accounts = Accounts.objects.get(admin=accounts_id)
    try:
        accounts.delete()
        messages.success(request, "Accountant Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_accounts"))
    except:
        messages.error(request, "Failed To Delete Accountant")
        return HttpResponseRedirect(reverse("manage_accounts"))
    
    
def delete_student(request, student_id):
    student = Student.objects.get(admin=student_id)
    try:
        student.delete()
        messages.success(request, "Student Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_student"))
    except:
        messages.error(request, "Failed To Delete Student")
        return HttpResponseRedirect(reverse("manage_student"))
    
    
def delete_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    try:
        course.delete()
        messages.success(request, "Course Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_course"))
    except:
        messages.error(request, "Failed To Delete Course")
        return HttpResponseRedirect(reverse("manage_course"))
    
    
def delete_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    try:
        subject.delete()
        messages.success(request, "Subject Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_subject"))
    except:
        messages.error(request, "Failed To Delete Subject")
        return HttpResponseRedirect(reverse("manage_subject"))
    
    
def delete_stage(request, stage_id):
    stage = Stages.objects.get(id=stage_id)
    try:
        stage.delete()
        messages.success(request, "Class Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_stage",kwargs={"stage_id":stage_id}))
    except:
        messages.error(request, "Failed To Delete Class")
        return HttpResponseRedirect(reverse("manage_stage",kwargs={"stage_id":stage_id}))
    
    
def delete_session(request, session_id):
    session = SessionYearModel.objects.get(id=session_id)
    try:
        session.delete()
        messages.success(request, "Session Year Deleted Successfully")
        return HttpResponseRedirect(reverse("manage_session"))
    except:
        messages.error(request, "Failed To Delete Session Year")
        return HttpResponseRedirect(reverse("manage_session"))
    
    
    

