from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("list/", views.users_list, name="list"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("<int:user_id>/", views.user_profile, name="profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("logout/", views.logout_view, name="logout"),
]