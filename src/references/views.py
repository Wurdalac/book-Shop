from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView,ListView,DeleteView,CreateView

from . import forms
from references.models import City
# Create your views here.


def cities_list(request):
    cities = City.objects.all()
    context = {"cities": cities}
    return render(request, template_name="cities.html", context = context)

class CitiesList(ListView):
    model=City

def city_detail(request, pk):
    city = City.objects.get(pk=pk)
    context = {"object": city}
    return render(request, template_name="detail.html", context = context)


class CityDetail(DetailView):
    model=City


def city_delete(request, pk):
    city = City.objects.get(pk=pk)
    message = f'City {city.name} addresses has just been deleted'
    city.delete()
    context = {"message": message}
    return render(request, template_name='delete.html', context=context)


class CityDelete(DeleteView):
    success_url=reverse_lazy('cities-list-cbv')
    model=City



def city_create(request):
    context = {}
    if request.method =='POST':
        form = forms.CityForm(request.POST)
        if form.is_valid():
            city = form.save()
            return HttpResponseRedirect(reverse('city-detail', kwargs={'pk':city.pk}))
        else:
            context ['form'] = form 
    else:
        context['form'] = forms.CityForm() 
    return render(request, template_name="create.html", context=context)



class CityCreate(CreateView):
    model=City  
    success_url=reverse_lazy('cities-list-cbv')
    fields=('name', 'description')
    #form_class = forms.CityForm





def city_update(request, pk):
    context = {}
    if request.method == "GET":
        city = City.objects.get(pk=pk)
        context = {'name': city.name, 'description': city.description}
    elif request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        city = City.objects.get(pk=pk)
        city.name = name
        city.description = description
        city.save()
        return HttpResponseRedirect(reverse('city-detail', kwargs={'pk':city.pk}))
    context = {}
    return render(request, template_name="create.html", context=context)
