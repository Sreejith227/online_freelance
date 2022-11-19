from django import forms
from importlib.abc import ExecutionLoader
from pyexpat import model
from statistics import mode
from django import forms
from core import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeedbackModel

        exclude = ('status',)