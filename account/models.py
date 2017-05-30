from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UcUserManager

# (id, name, is_admin, is_active, user_id, passwd, group_id, post_id, email, description, photo, department, major, )

type_list = (
    ("defualt", "미인증"),
    ("student", "인증"),
    ("company", "업자"),
)

class UcUser(AbstractBaseUser, PermissionsMixin):

    # 고유 키
    user_id = models.CharField(max_length=16, unique=True, primary_key=True)

    # 로그인 id
    login_id = models.CharField(max_length=16, unique=True)

    # 실명
    name = models.CharField(max_length=20)

    # 동아리 관리자인가
    is_admin = models.BooleanField(default=False)

    # 유니스트 메일
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    # 학생받았는지 메일 인증유무 혹은 업자유무
    type = models.CharField(choices=type_list, max_length=15, null=False)

    # 간략한 소개
    description = models.CharField(max_length=255, null=False, blank=True)

    # 사진
    photo = models.ImageField(
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
    )

    # 전공(선택)
    major = models.CharField(max_length=30)
    # 부전공(선택)
    minor = models.CharField(max_length=30)




    objects = UcUserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = ['name', 'email']



    def get_name(self):
        '''
        Returns the name for the user.
        '''
        return self.name
