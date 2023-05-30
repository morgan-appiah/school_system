"""
URL configuration for school_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from school_system import settings
from school_system_app import views, HodViews

urlpatterns = [
    path('', views.ShowLandPage),
    path('admin/', admin.site.urls),
    path('login_page', views.ShowLoginPage, name='login_page'),
    path('get_user_details', views.GetUserDetails, name='get_user_details'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('dologin', views.DoLogin, name='dologin'),
    path('admin_home', HodViews.admin_home, name='admin_home'),
    path('add_staff', HodViews.add_staff, name='add_staff'),
    path('add_staff_save', HodViews.add_staff_save, name='add_staff_save'),
    path('add_employee', HodViews.add_employee, name='add_employee'),
    path('add_employee_save', HodViews.add_employee_save, name='add_employee_save'),
    path('add_accounts', HodViews.add_accounts, name='add_accounts'),
    path('add_accounts_save', HodViews.add_accounts_save, name='add_accounts_save'),
    path('add_session', HodViews.add_session, name='add_session'),
    path('add_session_save', HodViews.add_session_save, name='add_session_save'),
    path('add_course', HodViews.add_course, name='add_course'),
    path('add_course_save', HodViews.add_course_save, name='add_course_save'),
    path('add_subject', HodViews.add_subject, name='add_subject'),
    path('add_subject_save', HodViews.add_subject_save, name='add_subject_save'),
    path('add_stage', HodViews.add_stage, name='add_stage'),
    path('add_stage_save', HodViews.add_stage_save, name='add_stage_save'),
    path('add_student', HodViews.add_student, name='add_student'),
    path('add_student_save', HodViews.add_student_save, name='add_student_save'),
    path('add_parent', HodViews.add_parent, name='add_parent'),
    path('add_parent_save', HodViews.add_parent_save, name='add_parent_save'),
    path('manage_staff', HodViews.manage_staff, name='manage_staff'),
    path('staff_profile/<str:staff_id>', HodViews.staff_profile, name='staff_profile'),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('manage_employee', HodViews.manage_employee, name='manage_employee'),
    path('employee_profile/<str:employee_id>', HodViews.employee_profile, name='employee_profile'),
    path('edit_employee/<str:employee_id>', HodViews.edit_employee, name="edit_employee"),
    path('edit_employee_save', HodViews.edit_employee_save, name="edit_employee_save"),
    path('manage_parent', HodViews.manage_parent, name='manage_parent'),
    path('parent_profile/<str:parent_id>', HodViews.parent_profile, name='parent_profile'),
    path('edit_parent/<str:parent_id>', HodViews.edit_parent, name="edit_parent"),
    path('edit_parent_save', HodViews.edit_parent_save, name="edit_parent_save"),
    path('manage_accounts', HodViews.manage_accounts, name='manage_accounts'),
    path('accounts_profile/<str:accounts_id>', HodViews.accounts_profile, name='accounts_profile'),
    path('edit_accounts/<str:accounts_id>', HodViews.edit_accounts, name="edit_accounts"),
    path('edit_accounts_save', HodViews.edit_accounts_save, name="edit_accounts_save"),
    path('manage_student', HodViews.manage_student, name='manage_student'),
    path('student_profile/<str:student_id>', HodViews.student_profile, name='student_profile'),
    path('edit_student/<str:student_id>', HodViews.edit_student, name="edit_student"),
    path('edit_student_save', HodViews.edit_student_save, name="edit_student_save"),
    path('manage_session', HodViews.manage_session, name='manage_session'),
    path('edit_session/<str:session_id>', HodViews.edit_session, name="edit_session"),
    path('edit_session_save', HodViews.edit_session_save, name="edit_session_save"),
    path('manage_course', HodViews.manage_course, name='manage_course'),
    path('edit_course/<str:course_id>', HodViews.edit_course, name="edit_course"),
    path('edit_course_save', HodViews.edit_course_save, name="edit_course_save"),
    path('manage_subject', HodViews.manage_subject, name='manage_subject'),
    path('edit_subject/<str:subject_id>', HodViews.edit_subject, name="edit_subject"),
    path('edit_subject_save', HodViews.edit_subject_save, name="edit_subject_save"),
    path('manage_stage', HodViews.manage_stage, name='manage_stage'),
    path('edit_stage/<str:stage_id>', HodViews.edit_stage, name="edit_stage"),
    path('edit_stage_save', HodViews.edit_stage_save, name="edit_stage_save"),


# STAFF URL



















]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
