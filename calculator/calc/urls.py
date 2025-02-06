from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    display_history_page,
    go_to_calc,
    index,
    history,
    save_calculation,
    history_page,
)

urlpatterns = [
    path("", index, name="calculator"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("save/", save_calculation, name="save_calculation"),
    path("history/", display_history_page, name="display_history_page"),
    path("history_elem/", history, name="history_elem"),
    path("history_page/", history_page, name="history_page"),
    path("go_to_calc/", go_to_calc, name="go_to_calc"),
]
