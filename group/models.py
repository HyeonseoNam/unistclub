from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from account.models import UcUser
# Create your models here.

status_list = (
    ("study", "스터디"),
    ("social", "친목모임"),
)

class GroupQueryset(models.query.QuerySet):
    def is_apply(self):
        return self.filter(is_apply=True)

class GroupManager(models.Manager):
    def get_queryset(self):
        return GroupQueryset(self.model, using=self._db)

    def is_apply(self):
        return self.get_queryset().is_apply()

# 그룹 이미지 받는 장소
def download_group_image(instance, filename):
    return "groups/%s/%s" % (instance.group_id, filename)

class Group(models.Model):

    # 고유 키
    group_id = models.CharField(max_length=16, unique=True, primary_key=True)

    # 그룹 이름
    group_name = models.CharField(max_length=255, null=False)

    # 종류(스터디, 친목모임 등)
    group_status = models.CharField(choices=status_list, max_length=15, null=False)

    # 그룹 이미지
    group_photo = models.ImageField(
        null=True,
        blank=True,
        upload_to=download_group_image
    )

    # 모임 시간
    meeting_time = models.CharField(max_length=255, null=True, blank=True)

    # 모임 장소
    meeting_place = models.CharField(max_length=255, null=True, blank=True)

    # 등록일
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    # 등록일
    modified_at = models.DateTimeField(auto_now=True)

    # 모임 소개
    description = models.CharField(max_length=255, null=False, blank=True)

    # 연락처 부분
    contact = models.CharField(max_length=255, null=False, blank=True)


    # 지원가능여부
    is_apply = models.BooleanField(default=False)

    # 상시모집여부
    is_always_apply = models.BooleanField(default=False)

    # 지원가능기간
    apply_start = models.DateField(auto_now=False)
    apply_end = models.DateField(auto_now=False)

    # 관리자 id
    admin = models.ForeignKey(UcUser, related_name="group_admin")

    # 지원가능인원
    max_member = models.PositiveIntegerField()

    # 유저
    members = models.ManyToManyField(UcUser, through='Membership')

    # Manager
    objects = GroupManager()

    @property
    def get_absolute_url(self):
        return reverse('group_detail', kwargs={"group_id": self.group_id})
    @property
    def get_group_photo(self):
        # TODO preprocess로 이미지 크기 미리 줄여주기
        # group_photo가 있는지 확인
        if self.group_photo:
            # local setting
            if settings.DEBUG:
                return settings.MEDIA_URL + '%s'%(self.group_photo)
            # production setting
            else:
                return '%s%s' % (settings.MEDIA_ROOT, self.media)
        #else:
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

class Membership(models.Model):
    member = models.ForeignKey(UcUser)
    group = models.ForeignKey(Group)
    date_joined = models.DateField(auto_now_add=True, auto_now=False)
    status = models.BooleanField(default=False)

class Comment(models.Model):
    group = models.ForeignKey(Group)
    user = models.ForeignKey(UcUser)
    content = models.CharField(max_length=255, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)