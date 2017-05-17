from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UcUserManager

# (id, name, is_admin, is_active, user_id, passwd, group_id, post_id, email, description, photo, department, major, )

class UcUser(AbstractBaseUser, PermissionsMixin):

    user_id = models.CharField(_('user id'), max_length=16, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('full name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    # is_admin?
    # group_id?
    # post_id?
    # description 간단한 자기소개
    # photo 프로필 사진
    # department 뭐였더라?
    # major

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UcUserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
