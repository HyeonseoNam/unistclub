from django.db import models

# Create your models here.

type_list = (
    ("study", "스터디"),
    ("social", "친목모임"),
)

class Group(models.Model):

    # 그룹 이름
    group_name = models.CharField(max_length=30, null=False)

    # 종류(스터디, 친목모임 등)
    group_status = models.CharField(max_length=15, null=True, blank=True)

    # 등록일
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    # 등록일
    modified_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    # 모임 소개
    description = models.CharField(max_length=255, null=False, blank=True)

    # 지원가능여부
    is_apply = models.BooleanField(default=False)

    # 상시모집여부
    is_always_apply = models.BooleanField(default=False)

    # 지원가능기간
    apply_start = models.DateField(auto_now=False)
    apply_end = models.DateField(auto_now=False)

    # 관리자 id
    admin_id = models.PositiveIntegerField()