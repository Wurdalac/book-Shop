from django.contrib import admin

# Register your models here.
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'date'
    ]

admin.site.register(News, NewsAdmin)

from .models import City


class CityAdmin(admin.ModelAdmin):
    search_fields = ['name__name']
    list_display = [
        'pk',
        'name',
        'description',
    ]

admin.site.register(City, CityAdmin)


from .models import Genres

class GenresAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Genres, GenresAdmin)

from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name__name']
    list_display = [
        'first_name',
        'last_name',
        'middle_name'
    ]

admin.site.register(Author, AuthorAdmin)


