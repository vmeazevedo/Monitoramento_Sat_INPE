import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import requests
from drawnow import *

# API KEY: https://www.n2yo.com/api/
apiKey="<COLOQUE AQUI A SUA APIKEY>"

# Função de requisição de dados do satélite
def amazonia_1():   
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/47699/-23.635/-46.478/0/1/&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def nanosat_c_br1():
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/40024/-23.635/-46.478/0/1/&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def saci_1():
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/25941/-23.635/-46.478/0/1/&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def scd_2():
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/25504/-23.635/-46.478/0/1/&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def scd_1():
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/22490/-23.635/-46.478/0/1/&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def oscar_17():
    url = 'https://api.n2yo.com/rest/v1/satellite/positions/20440/-23.635/-46.478/0/1/&&apiKey=' + apiKey +'"'
    resposta = requests.get(url)
    dados = resposta.json()
    return dados

def live_stream():
    # # SATELITE AMAZONIA 1
    info_amazonia_1 = amazonia_1()
    longitude_amazonia_1 = info_amazonia_1['positions'][0]['satlongitude']
    latitude_amazonia_1 = info_amazonia_1['positions'][0]['satlatitude']

    # SATELITE NANOSAT C-BR1
    info_nanosat_c_br1 = nanosat_c_br1()
    longitude_nanosat_c_br1 = info_nanosat_c_br1['positions'][0]['satlongitude']
    latitude_nanosat_c_br1 = info_nanosat_c_br1['positions'][0]['satlatitude']   

    # SATELITE SACI 1
    info_saci_1 = saci_1()
    longitude_saci_1 = info_saci_1['positions'][0]['satlongitude']
    latitude_saci_1 = info_saci_1['positions'][0]['satlatitude']

    # SATELITE SCD 2
    info_scd_2 = scd_2()
    longitude_scd_2 = info_scd_2['positions'][0]['satlongitude']
    latitude_scd_2 = info_scd_2['positions'][0]['satlatitude']

    # SATELITE SCD 1
    info_scd_1 = scd_1()
    longitude_scd_1 = info_scd_1['positions'][0]['satlongitude']
    latitude_scd_1 = info_scd_1['positions'][0]['satlatitude']

    # SATELITE OSCAR 17
    info_oscar_17 = oscar_17()
    longitude_oscar_17 = info_oscar_17['positions'][0]['satlongitude']
    latitude_oscar_17 = info_oscar_17['positions'][0]['satlatitude']

    map = Basemap(
        projection='cyl',
        resolution="c",            
        llcrnrlat=-90,
        urcrnrlat=90,
        llcrnrlon=-180,
        urcrnrlon=180, 
        )
    
    map.bluemarble()
    map.drawcountries(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
    map.drawstates(linewidth=0.8, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)

    map.drawparallels(np.arange(-90,90,30),labels=[1,1,0,1], fontsize=8)
    map.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1], rotation=45, fontsize=8)

    date = datetime.utcnow()
    map.nightshade(date)

    x, y = map(longitude_amazonia_1, latitude_amazonia_1)
    plt.plot(x, y, '*', color='white', markersize=7)
    plt.text(x, y, ' AMAZONIA 1',color='white', fontsize=9)

    x1, y1 = map(longitude_nanosat_c_br1, latitude_nanosat_c_br1)
    plt.plot(x1, y1, '*', color='white', markersize=7)
    plt.text(x1, y1, ' NANOSAT C-BR1',color='white', fontsize=9)

    x2, y2 = map(longitude_saci_1, latitude_saci_1)
    plt.plot(x2, y2, '*', color='white', markersize=7)
    plt.text(x2, y2, ' SACI 1',color='white', fontsize=9)

    x3, y3 = map(longitude_scd_2, latitude_scd_2)
    plt.plot(x3, y3, '*', color='white', markersize=7)
    plt.text(x3, y3, ' SCD 2',color='white', fontsize=9)

    x4, y4 = map(longitude_scd_1, latitude_scd_1)
    plt.plot(x4, y4, '*', color='white', markersize=7)
    plt.text(x4, y4, ' SCD 1',color='white', fontsize=9)

    x5, y5 = map(longitude_oscar_17, latitude_oscar_17)
    plt.plot(x5, y5, '*', color='white', markersize=7)
    plt.text(x5, y5, ' OSCAR 17',color='white', fontsize=9)

    plt.title('Dia/Noite - %s (UTC)' % date.strftime("%d %b %Y %H:%M:%S"))
    plt.xlabel('Longitude', labelpad=40, fontsize=9)
    plt.ylabel('Latitude', labelpad=40, fontsize=9)

while True:
    drawnow(live_stream)
    plt.pause(1)
