# models에서 정의한 class를 django 내 객체로 받도록 하는 역할

from django.contrib.auth.base_user import BaseUserManager
import random
# from .models import UcUser


# models에서 User
class UcUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login_id, name, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        user = self.model(login_id=login_id, name=name, email=self.normalize_email(email), **extra_fields)
        user.user_id = ''.join(random.sample('0123456789',5))
        """
        TODO - user의 random key id의 중복방지 추가하여야 함
        if UcUser.objects.filter(pk=newid).count() == 0:
        self.object_id = newid
        """
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login_id, name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login_id, name, email, password, **extra_fields)

    def create_superuser(self, login_id, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(login_id, password, **extra_fields)