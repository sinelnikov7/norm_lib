from .models import Client
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'