from django.contrib import admin
from django.shortcuts import redirect
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


def root(request):
    return redirect("projects:project_list")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", root),
    path("users/", include("users.urls")),
    path("projects/", include("projects.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
