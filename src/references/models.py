from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(
        verbose_name="City's name",
        max_length=50,
        )
    description = models.TextField(
        verbose_name="City's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

class News(models.Model):
    title = models.CharField(verbose_name='Title', max_length=30)
    anons = models.CharField(verbose_name='Anons', max_length=250)
    description= models.TextField(verbose_name='Description')
    date = models.DateTimeField(verbose_name='Publication date')
    
    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Genres(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(verbose_name='Genre description')

    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    book = models.TextField (verbose_name='The books he wrote')
    genres = models.ForeignKey(Genres, related_name='genres_author', on_delete =models.PROTECT)
    


    def __iter__(self):
        return self.first_name, self.last_name
    
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'