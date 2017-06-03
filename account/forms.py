import random
from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import UcUser
from django.utils.translation import ugettext, ugettext_lazy as _

from django.contrib.auth.forms import UsernameField
from django.contrib.auth import password_validation

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _("패스워드가 일치하지 않습니다."),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = UcUser
        fields = ("login_id", "name","email", "password1", "password2", "photo")
        field_classes = {'login_id': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        # self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        self.instance.login_id = self.cleaned_data.get('login_id')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.user_id = ''.join(random.sample('0123456789', 5))
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

