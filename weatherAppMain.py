import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/weather/today/l/2bae6c4d78c772e312bd407df4d2e25d94ee4a5d5ae9bda9653be119519380b0"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

img = Image.open(r"c:\Users\ajaym\Documents\WeatherApp\Weather.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    #Update class for location, temperature and HowSWeather using Browser inspect element funcationality
    location =soup.find('h1', class_="_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--location--1Ayv3").text
    temperature = soup.find('span', class_="_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--tempValue--3KcTQ").text
    HowSWeather=soup.find('div',class_="_-_-node_modules-@wxu-components-src-organism-CurrentConditions-CurrentConditions--phraseValue--2xXSr").text
    
    locationLabel.config(text=location)
    temperatureLabel.config(text=temperature)
    HowSWeatherLabel.config(text=HowSWeather)

    temperatureLabel.after(60000,getWeather)
    master.update()

locationLabel = Label(master, font=("Calibri bold", 20),bg="white")
locationLabel.grid(row=0, sticky = "N",padx=100)
temperatureLabel = Label(master,font=("Calibri bold",70), bg="white")
temperatureLabel.grid(row=1, sticky="W",padx=40)
HowSWeatherLabel = Label(master, font=("Calibri bold", 15), bg="white")
HowSWeatherLabel.grid(row=2,sticky="W", padx=40)
Label(master, image=img, bg="white").grid(row=1,sticky="E")

getWeather()
master.mainloop()
