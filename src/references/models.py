from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(
        verbose_name="City's name",
        max_length=20,
        )
    description = models.TextField(
        verbose_name="City's description",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name 


class News(models.Model):
    title = models.CharField(verbose_name='Title', max_length=30)
    anons = models.CharField(verbose_name='Anons', max_length=250)
    description= models.TextField(verbose_name='Description')
    date = models.DateTimeField(verbose_name='Publication date')
    
    def __str__(self):
        return self.title 
    
   
