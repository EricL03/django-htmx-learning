from django.contrib import admin
from .models import Calculation


@admin.register(Calculation)
class CalculationAdmin(admin.ModelAdmin):
    list_display = ("expression", "created_at")  # Columns in admin panel
