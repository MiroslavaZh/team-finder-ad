import re

from django.core.exceptions import ValidationError

from .constants import (
    GIT_HOST,
    INVALID_GIT_URL_MESSAGE,
    INVALID_PHONE_MESSAGE,
    PHONE_REGEX,
)


def validate_github_url(url):
    if url and GIT_HOST not in url:
        raise ValidationError(INVALID_GIT_URL_MESSAGE)
    return url


def validate_phone(phone):
    if not phone:
        return phone

    if not re.match(PHONE_REGEX, phone):
        raise ValidationError(INVALID_PHONE_MESSAGE)

    return phone
