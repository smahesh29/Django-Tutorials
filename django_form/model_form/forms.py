from django.forms import ModelForm, Textarea
from .models import Author, Book
from django.utils.translation import gettext_lazy as _

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']


class AuthorForm_1(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title']


class AuthorForm_2(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorForm_3(ModelForm):
    class Meta:
        model = Author
        exclude = ['title']


class AuthorForm_4(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class AuthorForm_5(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name': _('Writer'),
        }
        help_texts = {
            'name': _('Enter the writers name'),
        }

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']