from django.core.paginator import Paginator

from .constants import PROJECTS_PER_PAGE


def paginate_queryset(request, queryset):
    paginator = Paginator(queryset, PROJECTS_PER_PAGE)
    page = request.GET.get("page")
    return paginator.get_page(page)