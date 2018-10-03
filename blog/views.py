from django.shortcuts import render


def index(request):
    return render(request, "base.html")


def about(request):
    return render(request, "about.html")


def project(request):
    return render(request, "project.html")


def devlog(request):
    return render(request, "devlog.html")