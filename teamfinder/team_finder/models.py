from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .constants import (
    AVATAR_UPLOAD_PATH,
    USER_ABOUT_MAX_LENGTH,
    USER_NAME_MAX_LENGTH,
    USER_PHONE_MAX_LENGTH,
    USER_SURNAME_MAX_LENGTH,
)
from .managers import UserManager
from .services import generate_avatar


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)

    name = models.CharField(max_length=USER_NAME_MAX_LENGTH)
    surname = models.CharField(max_length=USER_SURNAME_MAX_LENGTH)

    avatar = models.ImageField(upload_to=AVATAR_UPLOAD_PATH, blank=True)

    phone = models.CharField(
        max_length=USER_PHONE_MAX_LENGTH,
        unique=True,
        blank=True,
    )

    github_url = models.URLField(blank=True)
    about = models.CharField(max_length=USER_ABOUT_MAX_LENGTH, blank=True)

    favorites = models.ManyToManyField(
        "projects.Project",
        related_name="interested_users",
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.pk and not self.avatar:
            generate_avatar(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email