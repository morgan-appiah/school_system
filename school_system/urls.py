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

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
