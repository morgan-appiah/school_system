from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
import json
import os

from django.urls import reverse

from school_system_app.EmailBackEnd import EmailBackEnd


# Create your views here.



def ShowLandPage(request):
    return render(request, "land_page.html")


def ShowLoginPage(request):
    return render(request,"login_page.html")

def DoLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user != None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect("/admin_home")
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("student_home"))
            elif user.user_type == "4":
                return HttpResponseRedirect(reverse("parent_home"))
            elif user.user_type == "5":
                return HttpResponseRedirect(reverse("accounts_home"))
            else:
                return HttpResponseRedirect(reverse("employee_home"))
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("login_page")


def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype : "+request.user.user_type)
    else:
        HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")
