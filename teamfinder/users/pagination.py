from django.core.paginator import Paginator

from .constants import USERS_PER_PAGE

def paginate_users(request, queryset):
    paginator = Paginator(queryset, USERS_PER_PAGE)
    page = request.GET.get("page")
    return paginator.get_page(page)