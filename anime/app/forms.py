from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
from app.models import Project, Genre, Status

class commentForm(forms.Form):       
    username = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control','placeholder': 'User name'}))
    text = forms.CharField(max_length=300, widget=forms.Textarea({'class': 'form-control', 'placeholder': 'Comment'}))
    captcha = CaptchaField()

class searchForm(forms.Form):
    genre_choices = [('Все, кроме 18+','Все, кроме 18+'), ('Все', 'Все')]
    genre_choices += [(i['name'], i['name']) for i in Genre.objects.values('name').distinct()]
    genre = forms.ChoiceField(choices=genre_choices)

    status_choices = [('Все', 'Все')]
    status_choices += [(i['name'], i['name']) for i in Status.objects.values('name').distinct()]
    status = forms.ChoiceField(choices=status_choices)
    #genre = forms.ModelChoiceField(required = False, queryset=Genre.objects.all(),widget=forms.Select())
    #status = forms.ModelChoiceField(required = False, queryset=Status.objects.all(),widget=forms.Select())