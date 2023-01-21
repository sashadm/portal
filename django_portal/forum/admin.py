from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

admin.site.register(ForumSection)
admin.site.register(ForumTheme)


class ForumMessageAdmin(SummernoteModelAdmin):
    list_display = ['text', 'created_at', 'user', 'theme']
    summernote_fields = ['text']


admin.site.register(ForumMessage,ForumMessageAdmin)

