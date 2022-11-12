from django.shortcuts import render, get_object_or_404
from .models import BlogEntry


def index(request):
    entries = BlogEntry.objects.all()
    return render(request, 'index.html', {'entries': entries})


def show_post(request,id):
    post = get_object_or_404(BlogEntry, id=id)
    return render(request, 'show.html', {'post': post})