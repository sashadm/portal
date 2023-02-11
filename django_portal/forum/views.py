from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import MessageForm
from django.shortcuts import redirect
from django.template.loader import render_to_string


def show_theme(request, id):
    print(request.user.id)
    theme = get_object_or_404(ForumTheme, id=id)
    form = None
    if request.method == 'GET':
        form = MessageForm(initial={'theme': theme})
        return render(request, 'forum/show_theme.html', {'theme': theme, 'form': form})
    if request.method == 'POST':
        form = MessageForm(request.POST)
        form.post_id = id
        #form.user.id = request.user.id
        if form.is_valid():
            form.save()
        #form = MessageForm(initial={'theme': theme})
        return redirect(f'/theme/{id}')


def index(request):
    sections = ForumSection.objects.all()
    return render(request, 'forum/index.html', {'sections': sections})
