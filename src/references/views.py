from django.shortcuts import render
from django.http import HttpResponse

from references.models import City
# Create your views here.

def home_page(request):
    return render(request, template_name="home.html")

def cities_list(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, template_name="cities.html", context = context)
