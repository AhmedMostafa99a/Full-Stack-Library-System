from django.forms import ModelForm
from django.db import *
from .models import *
from django import form
class personForm(form.Form):
    firstname = form.CharField(max_length=100)
    lastname = form.CharField(max_length=100)
