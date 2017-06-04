from django.conf import settings
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

# 그룹 이미지 받는 장소
def download_user_image(instance, filename):
    return "users/%s/%s" % (instance.user_id, filename)

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
        blank=True,
        null=True,
        upload_to=download_user_image
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

    @property
    def get_user_photo(self):
        # TODO preprocess로 이미지 크기 미리 줄여주기
        # group_photo가 있는지 확인
        if self.photo:
            # local setting
            if settings.DEBUG:
                return settings.MEDIA_URL + '%s' % (self.photo)
            # production setting
            else:
                return '%s%s' % (settings.MEDIA_ROOT, self.media)
        # else:
        # TODO 소셜 로그인시 사진 가져오기
        # if social account
        # if SocialAccount.objects.filter(user_id=self.id):
        #     social_user = SocialAccount.objects.filter(user_id=self.id)
        #     if len(social_user):
        #         return "http://graph.facebook.com/{}/picture?width=100&height=100".format(social_user[0].uid)
        # # no profile
        # else:
        #     # 유저 이메일 주소에 따라 1~3 숫자로 변환
        #     pseudo_random_num = int(int(self.email.encode('hex'), 16) % 3) + 1
        #     random_profile = static('img/no_profile_' + str(pseudo_random_num) + '.png')
        #     return random_profile
