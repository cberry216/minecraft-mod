from django.contrib import admin
from django.shortcuts import redirect

from .models import Mod

# Register your models here.


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'description')
    search_fields = ('title', 'description')
    ordering = ('title',)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('index')

    def response_change(self, request, obj):
        return redirect('index')
