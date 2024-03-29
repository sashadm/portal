from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import BlogEntry
from .forms import CommentForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers


def index(request):
    entries = BlogEntry.objects.all()
    print(request.user)
    return render(request, 'index.html', {'entries': entries})


@login_required
def show_post(request, id):
    post = get_object_or_404(BlogEntry, id=id)
    comments = post.comments.all().order_by('-created_at')
    paginator = Paginator(comments, 5)
    form = None
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'GET':
        form = CommentForm(initial={'post': post})
        return render(request, 'show.html', {'page_obj': page_obj, 'post': post, 'form': form})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.post_id = id
        if form.is_valid():
            form.save()
    return redirect(f'/post/{id}')


def show_post_json(request, id):
    post = get_object_or_404(BlogEntry, id=id)
    return JsonResponse({'post': serializers.serialize('json', [post])})