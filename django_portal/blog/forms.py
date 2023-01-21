from django.forms import ModelForm
from .models import *
from django import forms


class CommentForm(ModelForm):
    post = forms.ModelChoiceField(label='post', queryset=BlogEntry.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['user', 'avatar']


