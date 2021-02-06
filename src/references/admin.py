from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    search_fields = [name__name]
    list_display = [
        'title',
        'date'
    ]

admin.site.register(News, NewsAdmin)

from . import models 


class CityAdmin(admin.ModelAdmin):
    search_fields = ['name__name']
    list_display = [
        'pk',
        'name',
        'description',
    ]

admin.site.register(City, CityAdmin)


