from django.db import models

# Create your models here.

type_list = (
    ("regular", "정규"),
    ("preregular", "가등록"),
    ("irregular", "소모임"),
)

class Club(models.Model):
    # sns_type = models.CharField(choices=sns_type_list, max_length=15, null=False)

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

    # 멤버수
    num_of_memebers = models.PositiveIntegerField()

    # 포스트수
    num_of_posts = models.PositiveIntegerField()

    # 등록일
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    # url
    url = models.CharField()

    # 지원가능여부
    is_applicable = models.BooleanField(default=False)

    # 지원가능기간
    application_period = models.DateField()

    # 상시모집여부
    is_always_apply = models.BooleanField(default=False)

    # 지원 url (google)
    application_url = models.CharField()

    # 회장 user id
    #  = models.ForeignKey(Seller)seller = models.ForeignKey(Seller)
