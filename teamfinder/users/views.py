from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render

from projects.models import Project

from .forms import LoginForm, ProfileForm, RegisterForm
from .models import User
from projects.services import paginate_queryset
from .constants import USERS_PER_PAGE


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return redirect("users:login")

    return render(request, "users/register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        user = authenticate(
            request,
            email=form.cleaned_data["email"],
            password=form.cleaned_data["password"],
        )

        if user:
            login(request, user)
            return redirect("projects:project_list")

        form.add_error(None, "Неверные данные")

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("projects:project_list")


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)

    owned_projects = Project.objects.filter(owner=user)
    participated_projects = Project.objects.filter(participants=user)

    return render(
        request,
        "users/user-details.html",
        {
            "user": user,
            "owned_projects": owned_projects,
            "participated_projects": participated_projects,
        },
    )


@login_required
def edit_profile(request):
    form = ProfileForm(
        request.POST or None,
        request.FILES or None,
        instance=request.user,
    )

    if form.is_valid():
        form.save()
        return redirect("users:profile", user_id=request.user.id)

    return render(request, "users/edit_profile.html", {"form": form})


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user, request.POST or None)

    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect("users:profile", user_id=user.id)

    return render(request, "users/change_password.html", {"form": form})


def users_list(request):
    users = User.objects.all().order_by("-id")

    current_filter = request.GET.get("filter")

    if request.user.is_authenticated and current_filter:
        if current_filter == "owners-of-favorite-projects":
            users = users.filter(
                owned_projects__in=request.user.favorites.all()
            ).distinct()

        elif current_filter == "owners-of-participating-projects":
            users = users.filter(owned_projects__participants=request.user).distinct()

        elif current_filter == "interested-in-my-projects":
            users = users.filter(favorites__owner=request.user).distinct()

        elif current_filter == "participants-of-my-projects":
            users = users.filter(participated_projects__owner=request.user).distinct()

    users_page = paginate_queryset(
        request=request,
        queryset=users,
        per_page=USERS_PER_PAGE,
    )

    return render(
        request,
        "users/participants.html",
        {
            "participants": users_page,
            "active_filter": current_filter,
        },
    )
