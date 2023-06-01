from django.shortcuts import render


def employee_home(request):
    return render(request, "employee_templates/home_content.html")