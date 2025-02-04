from django.shortcuts import render


def index(request):
    return render(request, "calc/index.html")


def history(request):
    return render(request, "calc/history.html")
