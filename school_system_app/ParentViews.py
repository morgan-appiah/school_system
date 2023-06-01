from django.shortcuts import render


def parent_home(request):
    return render(request, "parent_templates/home_content.html")