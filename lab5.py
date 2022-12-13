import requests
import tkinter as tk
from tkinter import messagebox


def get_weather():
    print("Введите название города")
    city = input()
    weather_key = "69567d896e8880df9ef919e8a9f097c8"
    try:
        weather_request = requests.get(
            'https://api.openweathermap.org/data/2.5/weather',
            par={'q':city, 'appid': weather_key, 'units': 'metric', 'lang': 'ru'})
        weather = weather_request.json()
        description = weather.get('weather')[0].get('description')
        temp = weather.get('main').get('temp')
        wind = weather.get('wind').get('speed')
        print("Ваш город: " + city)
        print("Погода на данный момент - %s, %.1f°C. Скорость ветра %.1f м/с" % (description, temp, wind))
    except Exception:
        print("Еще раз?")
        if input() == 'yes':
            get_weather()
    print("Еще?")
    if input() == 'yes':
        get_weather()

def find_ISS():
    try:
        iss_url = "http://api.open-notify.org/iss-now.json"
        iss_request = requests.get(iss_url)
        iss_json = iss_request.json()
        lon = iss_json.get("iss_position").get("longitude")
        lat = iss_json.get("iss_position").get("latitude")
        print("Положение МКС на данный момент")
        print("Широта: %s" % (lat))
        print("Долгота: %s" % (lon))
    except Exception:
        print("Не удалось найти МКС")

def astros():
    try:
        astros_url = "http://api.open-notify.org/astros.json"
        astros_request = requests.get(astros_url)
        astros_json = astros_request.json()
        for i in astros_json.get("people"):
            print("Имя: %s, космический аппарат: %s" % (i.get("name"), i.get('craft')))
        print("Всего человек: %s" % (astros_json.get("number")))
    except Exception:
        print("Не удалось посчитать")


def try_requests():
    try:
        r = requests.get("http://open-notify.org")
        print(r)
    except Exception:
        print("Что-то пошло не так")

def get_kitten():
   url = 'https://aws.random.cat/meow'
   try:
       cats_request = requests.get(url)
       pic_url = cats_request.json().get('file')
       pic_res = requests.get(pic_url)
       buffer = open("Buffer", 'wb')
       buffer.write(pic_res.content)
       buffer.close()
       img = Image.open("Buffer")
       img = img.resize((500, 500), Image.Resampling.LANCZOS)
       image = ImageTk.PhotoImage(img)
       label.config(image=image)
       label.image = image
       img.close()
   except Exception:
       messagebox.showerror("Ошибка", "Не удалось установить соединение")




try_requests()
get_weather()
astros()
find_ISS()
