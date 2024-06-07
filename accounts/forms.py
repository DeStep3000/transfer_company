import re

from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Пароль должен содержать не менее 8 символов, не быть слишком простым и не быть похожим на другие ваши личные данные.",
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Для подтверждения введите, пожалуйста, пароль ещё раз.",
    )
    phone_number = forms.CharField(
        label="Номер телефона",
        help_text="Введите номер телефона в международном формате (например, +1234567890)."
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'phone_number', 'password1', 'password2')
        labels = {
            'username': 'Имя пользователя',
            'phone_number': 'Номер телефона',
        }
        help_texts = {
            'username': '',
        }
        error_messages = {
            'username': {
                'max_length': "Это имя пользователя слишком длинное.",
            },
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        pattern = re.compile(r'^\+\d{1,15}$')
        if not pattern.match(phone_number):
            raise forms.ValidationError(
                "Введите номер телефона в правильном международном формате (например, +1234567890).")
        return phone_number


class VerifyPhoneForm(forms.Form):
    code = forms.CharField(max_length=6, label='Код подтверждения')
