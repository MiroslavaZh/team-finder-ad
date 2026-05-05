from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, password=None):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, surname, password):
        user = self.create_user(email, name, surname, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user