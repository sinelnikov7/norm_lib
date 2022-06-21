from django.forms import ModelForm

from .models import ActGiveOut


class ActGiveOutForm(ModelForm):
    class Meta:
        model = ActGiveOut
        fields = '__all__'
