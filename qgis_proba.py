# -*- coding: cp1250 -*-
import urllib
import json
from pprint import *
#URL
wroclaw ='http://api.openweathermap.org/data/2.5/group?id=3096053,3081368,3093692,3097257,3102987,3082707,3099828,3084093,3092931,3103096,3090205,3083103,3084404,3080231,3090170,3097367,3099213&units=metric'
#print wroclaw

#drukuje plik json
wroclaw2 = urllib.urlopen(wroclaw)
plik = json.load(wroclaw2)
with open("wroclaw_dump.json", 'w') as update:
    mf = json.dump(plik, update)
#print plik
wroclaw2.close()



pprint(plik)

#tablica parametrów pogody, pod nazwą klucza 'list'
pogoda = plik["list"]
#pprint(pogoda)
#potem biorę sobie pierwszy obiekt
wrocek = pogoda[0]
#print wr

#wspolrzedne
WrWsp = wrocek['coord']
print WrWsp

WrWsp = wrocek['coord'].values()
print WrWsp

WrWsp = wrocek['coord']['lon']
print WrWsp

WrNaz = wrocek['name']
print WrNaz

#zeby dostac sie do temperatury trzeba kolejna zmienna utworzyc z kluczem
Wrtemp = wrocek['main']['temp_min']
print Wrtemp

Wropis = wrocek['weather'][0]['main']
print Wropis

#pętla do zapisu danych do tablicy
prognozaPog = []
for i in range(0, len(pogoda)):
    miasto = pogoda[i]['name']
    wspolrzedne = pogoda[i]['coord'].values()
    temp = pogoda[i]['main']['temp']
    tempMax = pogoda[i]['main']['temp_max']
    tempMin = pogoda[i]['main']['temp_min']
    cisnienie = pogoda[i]['main']['pressure']
    wilgotnosc = pogoda[i]['main']['humidity']
    predkoscWiatru = pogoda[i]['wind']['speed']
    kierWiatru = pogoda[i]['wind']['deg']
    chmury = pogoda[i]['clouds']['all']
 #   opisPogody = pogoda[i]['weather']['desciption']
 #   ikonaPogody = pogoda[i]['weather']['main']
    

    prognozaDict = [miasto,wspolrzedne,temp,tempMax,tempMin,cisnienie,wilgotnosc,predkoscWiatru,kierWiatru,chmury]
    prognozaPog.append(prognozaDict)
print prognozaPog
