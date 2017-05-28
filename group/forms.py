from django import forms

from .models import (
    Group
)

class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Group
        fields = (
            'group_name',
            'group_status',
            'meeting_time',
            'meeting_place',
            'description',
            'contact',
            'is_apply',
            'is_always_apply',
            'apply_start',
            'apply_end',
        )