from datetime import date
from .models import Group

def update_is_apply():
    groups = Group.objects.all()
    for group in groups:
        if group.apply_start <= date.today() and date.today() <= group.apply_end:
            group.is_apply = True
            group.save()
        else:
            group.is_apply = False
            group.save()