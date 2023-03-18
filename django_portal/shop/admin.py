from django.contrib import admin
from .models import *

admin.site.register(Rubric)
admin.site.register(Section)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']


admin.site.register(Product, ProductAdmin)
