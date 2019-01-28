from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import ShopUser

from django.contrib.auth import models as auth_models
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'password1', 'password2',
                  'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Молодой')

        return age

    def clean_first_name(self):
        first_name: str = self.cleaned_data['first_name']

        return first_name.capitalize()

    def clean_password1(self):
        return validate_password_strength(self.cleaned_data['password1'])

def validate_password_strength(value):
    min_length = 10
    if len(value) < min_length:
        raise forms.ValidationError((
            'У пароля должно быть как минимум {0} символов.').format(min_length), code='ошибка!!!')

    if sum(c.isdigit() for c in value) < 2:
        raise ValidationError(('Пароль должен содержать как минимум 2 цифры.'), code='ошибка!!!')

    if not any(c.isupper() for c in value):
        raise ValidationError(('Пароль должен содержать как минимум одну заглавную букву.'), code='ошибка!!!')

    return value

class AdminPasswordChangeForm(auth_forms.AdminPasswordChangeForm):
    def clean_password1(self):
        return validate_password_strength(self.cleaned_data['password1'])

class UserAdmin(auth_admin.UserAdmin):
    change_password_form = AdminPasswordChangeForm
    add_form = UserCreationForm


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = ('first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18:
            raise forms.ValidationError('Молодой')

        return age
