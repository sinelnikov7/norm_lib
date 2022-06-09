from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        help_texts = {
            'username': None,
        }

        widgets = {
            'username': TextInput(attrs={
                'class':'label_style',
                'placeholder':'Введите логин'
            }),
            'first_name': TextInput(attrs={
                'class': 'label_style',
                'placeholder': 'Имя'
            }),
            'last_name': TextInput(attrs={
                'class': 'label_style',
                'placeholder': 'Фамилия'
            }),
            'email': TextInput(attrs={
                'class': 'label_style',
                'placeholder': 'Email',
                'type':'email'
            }),
            'password': TextInput(attrs={
                'class': 'label_style',
                'placeholder': 'Пароль',
                'type': 'password'
            })

        }