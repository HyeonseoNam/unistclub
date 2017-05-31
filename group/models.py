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

class Group(models.Model):

    # 그룹 이름
    group_name = models.CharField(max_length=255, null=False)

    # 종류(스터디, 친목모임 등)
    group_status = models.CharField(choices=status_list, max_length=15, null=False)

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
        return reverse('group_detail', kwargs={"group_id": self.id})

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