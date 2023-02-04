from django.shortcuts import render, get_object_or_404
from .models import *
from django.template.loader import render_to_string


def show_theme(request, id):
    theme = get_object_or_404(ForumTheme, id=id)
    return render(request, 'forum/show_theme.html', {'theme': theme})


def index(request):
    sections = ForumSection.objects.all()
    return render(request, 'forum/index.html', {'sections': sections})
