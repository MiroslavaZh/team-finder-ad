from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .constants import JSON_STATUS_OK, PROJECT_STATUS_CLOSED, PROJECT_STATUS_OPEN
from .forms import ProjectForm
from .models import Project
from .services import paginate_queryset


def project_list(request):
    queryset = (
        Project.objects.select_related("owner")
        .prefetch_related("participants")
        .order_by("-created_at")
    )

    projects = paginate_queryset(request, queryset)

    return render(
        request,
        "projects/project_list.html",
        {"projects": projects},
    )


def project_detail(request, project_id):
    project = get_object_or_404(
        Project.objects.select_related("owner").prefetch_related("participants"),
        id=project_id,
    )

    return render(
        request,
        "projects/project-details.html",
        {"project": project},
    )


@login_required
def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        project = form.save(commit=False)
        project.owner = request.user
        project.save()
        project.participants.add(request.user)

        return redirect(
            "projects:project_detail",
            project_id=project.id,
        )

    return render(
        request,
        "projects/create-project.html",
        {"form": form, "is_edit": False},
    )


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user,
    )

    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect(
            "projects:project_detail",
            project_id=project.id,
        )

    return render(
        request,
        "projects/create-project.html",
        {"form": form, "is_edit": True},
    )


@login_required
def complete_project(request, project_id):
    project = get_object_or_404(
        Project,
        id=project_id,
        owner=request.user,
    )

    if project.status == PROJECT_STATUS_OPEN:
        project.status = PROJECT_STATUS_CLOSED
        project.save()

    return JsonResponse(
        {
            "status": JSON_STATUS_OK,
            "project_status": PROJECT_STATUS_CLOSED,
        }
    )


@login_required
def toggle_participate(request, project_id):
    with transaction.atomic():
        project = Project.objects.select_for_update().get(id=project_id)
        user = request.user

        if is_participant := project.participants.filter(pk=user.pk).exists():
            project.participants.remove(user)
        else:
            project.participants.add(user)

        participants_count = project.participants.count()

    return JsonResponse(
        {
            "status": JSON_STATUS_OK,
            "participant": not is_participant,
            "participants_count": participants_count,
        }
    )


@login_required
def toggle_favorite(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if is_favorite := request.user.favorites.filter(id=project.id).exists():
        request.user.favorites.remove(project)
    else:
        request.user.favorites.add(project)

    return JsonResponse(
        {
            "status": JSON_STATUS_OK,
            "favorited": not is_favorite,
        }
    )


@login_required
def favorite_projects(request):
    projects = (
        request.user.favorites.select_related("owner")
        .prefetch_related("participants")
        .all()
    )

    return render(
        request,
        "projects/favorite_projects.html",
        {"projects": projects},
    )
