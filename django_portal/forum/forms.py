from django.forms import ModelForm
from .models import *
from django_summernote.widgets import SummernoteWidget
from django import forms


class MessageForm(ModelForm):
    theme = forms.ModelChoiceField(label='theme', queryset=ForumTheme.objects.all(), widget=forms.HiddenInput())
    text = forms.CharField(widget=SummernoteWidget(attrs={'summernote': {'width': '90%'}}))

    class Meta:
        model = ForumMessage
        fields = '__all__'
        exclude = ['user', 'avatar']
