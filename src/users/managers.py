from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as _UserManager
from users.constants.roles import Role


class UserManager(_UserManager):
    use_in_migrations = True

    def _create_user(self, email, first_name, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields["is_staff"] = False
        extra_fields["is_superuser"] = False
        extra_fields["role"] = Role.STUDENT
        # extra_fields["group"] = Group.INDIV

        return self._create_user(email, first_name, password, **extra_fields)

    def create_superuser(self, email=None, first_name=None, password=None, **extra_fields):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        extra_fields["role"] = Role.ADMIN
        # extra_fields["group"] = Group.OTHER

        return self._create_user(email, first_name, password, **extra_fields)
