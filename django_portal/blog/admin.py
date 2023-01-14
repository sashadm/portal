from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

admin.site.register(Rubric)
#admin.site.register(BlogEntry)
#admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','created_at']

admin.site.register(Comment, CommentAdmin)

class BlogEntryAdmin(SummernoteModelAdmin):
    list_display = ['title','text','created_at','rubric']
    summernote_fields = ['text']

admin.site.register(BlogEntry,BlogEntryAdmin)
