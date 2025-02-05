from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Calculation


@csrf_exempt  # ⬅️ Bypasses CSRF for this view
def save_calculation(request):
    if request.method == "POST":
        print("request: ", request.POST)

        result = request.POST.get("result", "").strip()
        expression = request.POST.get("expression", "").strip()

        if expression and result:
            # Save calculation to database
            Calculation.objects.create(expression=expression, result=result)

            # Return a partial HTML snippet to update the history section
            return HttpResponse(status=204)

        return HttpResponse(status=400)  # Bad request if no expression


def index(request):
    return render(request, "calc/index.html")


def display_history_page(request):
    return render(request, "calc/history.html")


def history(request):
    calculations = Calculation.objects.order_by("-created_at")  # Latest first
    return render(request, "calc/history_list.html", {"calculations": calculations})


@csrf_exempt  # ⬅️ Bypasses CSRF for this view
def go_to_calc(request):
    if request.headers.get("HX-Request"):
        return HttpResponse(headers={"HX-Redirect": "/"})  # Redirects in HTMX

    return redirect("")  # Normal Django redirect for non-HTMX requests


@csrf_exempt  # ⬅️ Bypasses CSRF for this view
def history_page(request):
    if request.headers.get("HX-Request"):
        return HttpResponse(headers={"HX-Redirect": "/history/"})  # Redirects in HTMX

    return redirect("history")  # Normal Django redirect for non-HTMX requests
