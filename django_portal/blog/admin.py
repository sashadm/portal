from django.contrib import admin

from .models import *

admin.site.register(Rubric)
admin.site.register(BlogEntry)
#admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text','created_at']

admin.site.register(Comment, CommentAdmin)
