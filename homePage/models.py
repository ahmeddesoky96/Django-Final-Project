from django.db import models
from django import forms

# Create your models here.


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, label='Search')
