#-*- coding: utf-8 -*-
from django import template
from group.models import Group
from group.models import Membership
from django.contrib.contenttypes.models import ContentType
import datetime, pytz

register = template.Library()

@register.filter(name='is_participating')
def is_participating(user_id, group_id):
    if not Membership.objects.filter(member=user_id, group=group_id).exists():
        # 참여하는게 없을때
        return 1
    else:
        membership = Membership.objects.get(member=user_id, group=group_id)
        # 참여중
        if membership.status == 1:
            return 2
        # 참여대기중
        else:
            return 3