from projects.services import paginate_queryset

from .constants import USERS_PER_PAGE


def paginate_users(request, queryset):
    return paginate_queryset(
        request=request,
        queryset=queryset,
        per_page=USERS_PER_PAGE,
    )
