from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import ActGiveOut


class ActGiveOutForm(ModelForm):
    def clean_books(self):
        books = self.cleaned_data['books']
        if len(books) > 5:
            raise ValidationError('Вы не можете выбрать более 5 книг')
        return books

    class Meta:
        model = ActGiveOut
        fields = ['client', 'count_of_day', 'books']
