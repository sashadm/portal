from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import BlogEntry
from .forms import CommentForm

def index(request):
    entries = BlogEntry.objects.all()
    return render(request, 'index.html', {'entries': entries})


def show_post(request,id):
    post = get_object_or_404(BlogEntry, id=id)
    comments = post.comments.all()
    paginator = Paginator(comments,3)
    form = None
    if request.method == 'GET':
        form = CommentForm(initial={'post': post})
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form.post_id = id
        if form.is_valid():
            form.save()
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'show.html', {'page_obj': page_obj, 'post': post,'form': form})