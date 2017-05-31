from django import forms

from .models import (
    Club
)

class ClubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Club
        fields = (
        )