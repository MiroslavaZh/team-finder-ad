from django.core.exceptions import ValidationError

from .constants import GIT_HOST, INVALID_GIT_URL_MESSAGE


def validate_git_url(url):
    if url and GIT_HOST not in url:
        raise ValidationError(INVALID_GIT_URL_MESSAGE)
    return url
