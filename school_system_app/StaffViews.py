from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def staff_home(request):
    return render(request, "staff_templates/base_template.html")