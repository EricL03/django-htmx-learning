from django.urls import path
from .views import index, history, save_calculation, history_page

urlpatterns = [
    path("", index, name="calculator"),
    path("save/", save_calculation, name="save_calculation"),
    path("history/", history, name="history"),
    path("history_page/", history_page, name="history_page"),
]
