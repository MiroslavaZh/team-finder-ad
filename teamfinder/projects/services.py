from django.core.paginator import Paginator

from .constants import PROJECTS_PER_PAGE


def paginate_queryset(
    request,
    queryset,
    per_page=PROJECTS_PER_PAGE,
):
    paginator = Paginator(queryset, per_page)
    page = request.GET.get("page")
    return paginator.get_page(page)
