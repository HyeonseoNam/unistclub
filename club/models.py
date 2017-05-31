from django.db import models
from account.models import UcUser

# Create your models here.

type_list = (
    ("regular", "정규"),
    ("preregular", "가등록"),
    ("irregular", "소모임"),
)

class Club(models.Model):

    # 이름
    name = models.CharField(max_length=10, null=False)

    # 카테고리(스포츠, 음악, 공연 등)
    category = models.CharField(max_length=25, null=True, blank=True)

    # 타입(정규, 가등록, 소모임)
    type = models.CharField(choices=type_list, max_length=15, null=False)

    # 소개
    description = models.CharField(max_length=255, null=False, blank=True)

    # 사진
    photo = models.ImageField(
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
        # upload_to=thumbnail_location
    )

    # 배경이미지(각 동아리 페이지에 배경으로 들어갈 이미지)
    background_image = models.ImageField(
        width_field="width",
        height_field="height",
        blank=True,
        null=True,
        # upload_to=thumbnail_location
    )

    # 메인 포스트
    # main_post_id  = models.ForeignKey(Post)
    main_post_id = models.PositiveIntegerField()

    # 멤버수
    num_of_memebers = models.PositiveIntegerField()

    # 포스트수
    num_of_posts = models.PositiveIntegerField()

    # 등록일
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    # url
    url = models.CharField(max_length=255)

    # 지원가능여부
    is_apply = models.BooleanField(default=False)

    # 상시모집여부
    is_always_apply = models.BooleanField(default=False)

    # 지원가능기간
    apply_start = models.DateField(auto_now=False)
    apply_end = models.DateField(auto_now=False)

    # 지원 url (google)
    apply_url = models.CharField(max_length=255)

    # 회장 user id
    leader_id  = models.ForeignKey(UcUser)
    # TODO : admin을 manytomany로 두고 그 중 1하면 leader로 두개하면 어떨까 - 일단 admin은 놔둠

    # 관리자 id
    # admin1_id = models.PositiveIntegerField()
    # admin2_id = models.PositiveIntegerField()