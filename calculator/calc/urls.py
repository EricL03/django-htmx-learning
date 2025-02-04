from django.urls import path
from .views import index, history

urlpatterns = [
    path("", index, name="calculator"),
    path("history/", history, name="history"),
]
