import random
from django import forms

from .models import (
    Group, Comment
)

class GroupForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)

        self.fields['description'].widget.attrs.update({
            'class' : 'materialize-textarea',
        })

        self.fields['apply_start'].widget.attrs.update({
            'class' : 'datepicker',
            'type' : 'date',
        })
        self.fields['apply_end'].widget.attrs.update({
            'class' : 'datepicker',
            'type' : 'date',
        })

        # template에 나타날 select 첫번째 문구설정
        choices = self.fields['group_status']._get_choices()
        choices[0] = ('', '그룹의 카테고리를 선택하세요.')
        self.fields['group_status']._set_choices(choices)


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
            'max_member',
            'group_photo'
        )
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
    def save(self, commit=True):
        group = super(GroupForm, self).save(commit=False)
        group.group_id = ''.join(random.sample('0123456789', 5))
        if commit:
            group.save()
        return group

class GroupChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupChangeForm, self).__init__(*args, **kwargs)

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
            'max_member',
            'group_photo'
        )
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
          'class' : 'materialize-textarea',
        })

    class Meta:
        model = Comment
        fields = (
            'content',
        )
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }