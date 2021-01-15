from django.contrib import admin
from . models import List
# Register your models here.

@admin.register(List)
class ListModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'start_time', 'end_time', 'desc']
