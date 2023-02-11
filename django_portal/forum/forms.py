from django.forms import ModelForm
from .models import *
from django import forms


class MessageForm(ModelForm):
    theme = forms.ModelChoiceField(label='theme', queryset=ForumTheme.objects.all(), widget=forms.HiddenInput())


    class Meta:
        model = ForumMessage
        fields = '__all__'
        exclude = ['user', 'avatar']
