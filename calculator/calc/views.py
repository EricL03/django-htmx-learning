from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Calculation
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)


@csrf_protect
def save_calculation(request):
    logger.info("In save_calculation")
    if request.method == "POST":
        print("request: ", request.POST)

        result = request.POST.get("result", "").strip()
        expression = request.POST.get("expression", "").strip()

        if expression and result:
            # Save calculation to database
            Calculation.objects.create(expression=expression, result=result)

            # Return a partial HTML snippet to update the history section
            return HttpResponse(status=204)

    logger.warning("No calculation could be saved")
    return HttpResponse(status=400)  # Bad request if no expression


@login_required
def index(request):
    return render(request, "calc/index.html")


def display_history_page(request):
    return render(request, "calc/history.html")


def history(request):
    calculations = Calculation.objects.order_by("-created_at")  # Latest first
    return render(request, "calc/history_list.html", {"calculations": calculations})


def go_to_calc(request):
    if request.headers.get("HX-Request"):
        return HttpResponse(headers={"HX-Redirect": "/"})  # Redirects in HTMX

    return redirect("")  # Normal Django redirect for non-HTMX requests


def history_page(request):
    if request.headers.get("HX-Request"):
        return HttpResponse(headers={"HX-Redirect": "/history/"})  # Redirects in HTMX

    return redirect("history")  # Normal Django redirect for non-HTMX requests
