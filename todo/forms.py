from django import forms
from django.forms import ModelForm

from .models import *


class Form(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = "__all__"