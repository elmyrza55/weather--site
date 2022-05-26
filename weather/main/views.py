from multiprocessing import Condition
from django.http import HttpRequest
from django.shortcuts import render
import requests
from googletrans import Translator

# Create your views here.title()
def index(request):
    city = 'OSH'
    country = 'Kyrgyzstan'
    cities = 'Osh','Bishkek','Batken'
    number = [4, 45, -7, 11, -58,47]
    return render(request,'index.html',context={'my_city':city,'my_country':country,'my_cities':cities,'numbers':number})


API_KEY ='f23d0f49e43c3d94254181ba645e43ef'
WETHER_API ='https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}'

def weather(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        print(city_name)
        
def weather(request):
    if request.method == 'POST':
        API_KEY ='f23d0f49e43c3d94254181ba645e43ef'
        city_name = request.POST.get('city')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'

        response = requests.get(url)
        data_dict = response.json()
        print(data_dict)
        icon_id = data_dict['weather'][0]['icon']
        translator = Translator()
        w_cond = translator.translate(data_dict['weather'][0]['description'], dest='ru').text
        Weather = f"Погода в городе {city_name.title()}:{w_cond}"
        
        temp = f"Температура в городе {city_name.title()}:{data_dict['main']['temp'] }°C"
        
        cond = translator.translate(data_dict['weather'][0]['main'],dest='ru').text
        
        Condition_weather = f"Прогноз погоды в городе {city_name.title()}:{cond}"
        
        Condition_weather = f"Прогноз погоды в городе {city_name.title()}:{data_dict['weather'][0]['main'] }"
        
        feels_like = f"Теьпература в городе {city_name.title()} ощущается как: {data_dict['main']['feels_like'] }°C"
        
        min_temp = f"Минимальная температура в городе {city_name.title()}:{data_dict['main']['temp_min'] }°C"
        
        max_temp = f"Максииальная температура в городе {city_name.title()}:{data_dict['main']['temp_max'] }°C"
        icon_id = data_dict['weather'][0]['icon']
        print(icon_id)
        
        return render(request,'index.html', context={'Weather':Weather,'temp':temp, 'condition_weather':Condition_weather,'feels_like':feels_like,'min_temp':min_temp, 'max_temp':max_temp, 'icon_id': icon_id})
    