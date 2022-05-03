from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests  
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f245e17d2076088c97ddb34f14a75c86'
    

    # Return all the cities in the database
    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weatherData = []

    template = loader.get_template('weather/index.html')

    for city in cities:

        city_weather = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
        }

        # Add weather to the list
        weatherData.append(weather)

    context = {
        'weatherData': weatherData,
        'form' : form
    }

    return HttpResponse(template.render(context, request))