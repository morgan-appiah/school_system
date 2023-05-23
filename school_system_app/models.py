from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class SessionYearModel(models.Model):
    id=models.AutoField(primary_key=True)
    semester_name=models.CharField(max_length=255)
    session_start_year=models.DateField(null=True, blank=True)
    session_end_year=models.DateField(null=True, blank=True)
    objects=models.Manager()


class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"), (4, "Parent"), (5, "Accounts"), (6, "Employees"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class PaymentMethod(models.Model):
    id=models.AutoField(primary_key=True)
    payment_method=models.CharField(max_length=255)
    payment_date=models.DateTimeField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Staff(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    puk=models.CharField(max_length=50, unique=True)
    address=models.TextField()
    salary=models.FloatField(default=0)
    allowance=models.FloatField(default=0)
    bank_name=models.CharField(max_length=255)
    bank_account=models.CharField(max_length=255)
    payment_date=models.DateField(null=True, blank=True)
    ezwich=models.CharField(max_length=255)
    momo_number=models.CharField(max_length=255)
    contact=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    profile_pic=models.FileField(default="")
    objects=models.Manager()


class Accounts(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    puk=models.CharField(max_length=50, unique=True)
    address=models.TextField()
    contact=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    profile_pic=models.FileField(default="")
    objects=models.Manager()


class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    puk=models.CharField(max_length=50, unique=True)
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    department=models.CharField(max_length=255)
    salary=models.FloatField(default=0)
    allowance=models.FloatField(default=0)
    bank_name=models.CharField(max_length=255)
    bank_account=models.CharField(max_length=255)
    payment_date=models.DateField(null=True, blank=True)
    ezwich = models.CharField(max_length=255)
    momo_number = models.CharField(max_length=255)
    role=models.CharField(max_length=255)
    qualification=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    profile_pic=models.FileField(default="")
    objects=models.Manager()


class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    puk=models.CharField(max_length=50, unique=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    puk=models.CharField(max_length=50, unique=True)
    subject_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.CASCADE,default=1)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Stages(models.Model):
    id=models.AutoField(primary_key=True)
    stage_name=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    staff_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Student(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    religion=models.CharField(max_length=255)
    mother=models.CharField(max_length=255)
    father=models.CharField(max_length=255)
    guardian_name=models.CharField(max_length=255)
    guardian_relationship=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    contact=models.CharField(max_length=50)
    emergency_contact=models.CharField(max_length=50)
    nonclass_activity=models.CharField(max_length=255)
    previous_health=models.CharField(max_length=255)
    previous_school=models.CharField(max_length=255)
    dob=models.DateField(blank=True, null=True)
    nationality=models.CharField(max_length=255)
    hometown=models.CharField(max_length=255)
    gps_address=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    alt_email=models.CharField(max_length=255)
    admission_date=models.DateField(null=True, blank=True)
    admission_number=models.CharField(max_length=50, unique=True)
    profile_pic=models.FileField()
    address=models.TextField()
    hostel=models.CharField(max_length=255)
    academic_tutor=models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    stage_id=models.ForeignKey(Stages, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()


class Parent(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    puk=models.CharField(max_length=50)
    ward=models.ForeignKey(Student, on_delete=models.CASCADE, default=1)
    address=models.TextField()
    contact=models.CharField(max_length=50)
    occupation=models.CharField(max_length=100)
    ward_tutor=models.ForeignKey(Staff, on_delete=models.CASCADE)
    tutor_contact=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    profile_pic=models.FileField(default="")
    objects=models.Manager()


class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    session_year_id=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class LeaveReportStudent(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class LeaveReportStaff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportParent(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class LeaveReportAcounts(models.Model):
    id = models.AutoField(primary_key=True)
    accounts_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    leave_date = models.CharField(max_length=255)
    leave_message = models.TextField()
    leave_status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackParent(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class FeedBackAccounts(models.Model):
    id = models.AutoField(primary_key=True)
    accounts_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationStaffs(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationParent(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.ForeignKey(Parent, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class NotificationAccounts(models.Model):
    id = models.AutoField(primary_key=True)
    accounts_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class StudentResult(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    stage_id=models.ForeignKey(Stages, on_delete=models.CASCADE)
    subject_exam_marks=models.FloatField(default=0)
    continuous_assessment=models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class OnlineClassRoom(models.Model):
    id=models.AutoField(primary_key=True)
    room_name=models.CharField(max_length=255)
    room_pwd=models.CharField(max_length=255)
    course_id=models.ForeignKey(Courses, on_delete=models.CASCADE)
    stage_id=models.ForeignKey(Stages, on_delete=models.DO_NOTHING)
    subject=models.ForeignKey(Subjects,on_delete=models.CASCADE)
    session_years=models.ForeignKey(SessionYearModel,on_delete=models.CASCADE)
    started_by=models.ForeignKey(Staff,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    created_on=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()


class Circular(models.Model):
    id=models.AutoField(primary_key=True)
    message=models.TextField()
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    objects=models.Manager()


class DisciplineRecords(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    message=models.TextField()
    record_date=models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class Schedule(models.Model):
    id=models.AutoField(primary_key=True)
    course_id=models.ForeignKey(Courses, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subjects, on_delete=models.CASCADE)
    start_time=models.DateTimeField(null=True, blank=True)
    end_time=models.DateTimeField(null=True, blank=True)
    day=models.CharField(max_length=255)
    session_year_id=models.ForeignKey(SessionYearModel, on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


class IncomeExpenditure(models.Model):
    id=models.AutoField(primary_key=True)
    fee_item=models.CharField(max_length=255)
    fee_amount=models.FloatField(default=0)
    status=models.BooleanField(default=False)
    amount_paid=models.FloatField(default=0)
    amount_due=models.FloatField(default=0)
    arrears=models.FloatField(default=0)
    balance=models.FloatField(default=0)
    expense_item=models.CharField(max_length=255)
    expense_amount=models.FloatField(default=0)
    grants_donors=models.FloatField(default=0)
    profit_loss=models.FloatField(default=0)
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)
    employee_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff, on_delete=models.CASCADE)
    session_year_id=models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    objects = models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance,address="",profile_pic="",contact="",puk="", bank_name="",
                                 bank_account="",ezwich="",momo_number="")
        if instance.user_type==3:
            Student.objects.create(admin=instance,course_id=Courses.objects.get(id=1),address="",
                                   profile_pic="",gender="",contact="",emergency_contact="",nationality="",
                                   religion="",nonclass_activity="",previous_health="",previous_school="",
                                   mother="",father="",academic_tutor=Staff.objects.get(id=1),
                                   stage_id=Stages.objects.get(id=1),hometown="",admission_number="",category="",
                                   gps_address="",alt_email="",hostel="",guardian_name="",guardian_relationship="")
        if instance.user_type==4:
            Parent.objects.create(admin=instance,address="",occupation="",puk="",ward=Student.objects.get(admission_number="RSS-0001-23"),
                                  ward_tutor=Staff.objects.get(id=1),contact="",tutor_contact="",profile_pic="")
        if instance.user_type==5:
            Accounts.objects.create(admin=instance,address="",contact="",puk="",profile_pic="")

        if instance.user_type==6:
            Employee.objects.create(admin=instance,address="",contact="",puk="",profile_pic="",department="",
                                    bank_name="",bank_account="",role="",qualification="",ezwich="",momo_number="")


@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.staff.save()
    if instance.user_type==3:
        instance.student.save()
    if instance.user_type == 4:
        instance.parent.save()
    if instance.user_type == 5:
        instance.accounts.save()
    if instance.user_type == 6:
        instance.employee.save()

