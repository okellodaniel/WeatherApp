from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests  

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f245e17d2076088c97ddb34f14a75c86'
    city = 'Las Vegas'

    city_weather = requests.get(url.format(city)).json()

    template = loader.get_template('weather/index.html')

    return HttpResponse(template.render(request))