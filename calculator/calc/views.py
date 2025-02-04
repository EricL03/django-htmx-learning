from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Calculation


@csrf_exempt  # ⬅️ Bypasses CSRF for this view
def save_calculation(request):
    if request.method == "POST":
        expression = request.POST.get("result", "").strip()

        if expression:
            # Save calculation to database
            Calculation.objects.create(expression=expression)

            # Return a partial HTML snippet to update the history section
            return HttpResponse(status=204)

        return HttpResponse(status=400)  # Bad request if no expression


def index(request):
    return render(request, "calc/index.html")


def history(request):
    calculations = Calculation.objects.order_by("-created_at")  # Latest first
    return render(request, "calc/history_list.html", {"calculations": calculations})
