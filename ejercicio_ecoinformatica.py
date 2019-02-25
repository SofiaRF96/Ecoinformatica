# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 10:17:08 2019

@author: Particular
"""

import pandas as pd
import folium

datos1=pd.read_csv('1esclavista.csv', sep= ',')
datos2=pd.read_csv('2esclava.csv', sep= ',')

location_corner=[38.27,-1.38]
specie1_map=folium.Map(location=location_corner, zoom_start=6, tiles='OpenStreetMap')
tooltip='Informacion sobre la especie: '

for label, ocurrence in datos1.iterrows():
    longitude = ocurrence['Longitud']
    latitude = ocurrence['Latitud']
    if not pd.isnull(longitude):
        filtro_ocurrencias = datos1[(datos1.Longitud==longitude) & (datos1.Latitud==latitude)]
        n_ocurrencias = filtro_ocurrencias.shape[0]
        marker=folium.Marker(
               location=[latitude, longitude],
               popup='<i>Rossomyrmex minuchae (hormiga esclavista) ' +  str(n_ocurrencias) + ' veces observada </i>',tooltip=tooltip,
               icon=folium.Icon(color='orange', icon='info-sign')
               )
        marker.add_to(specie1_map)

for label, ocurrence in datos2.iterrows():
    longitude = ocurrence['Longitud']
    latitude = ocurrence['Latitud']
    if not pd.isnull(longitude):
        filtro_ocurrencias = datos2[(datos2.Longitud==longitude) & (datos2.Latitud==latitude)]
        n_ocurrencias = filtro_ocurrencias.shape[0]
        marker=folium.Marker(
               location=[latitude, longitude],
               popup='<i>Proformica longiseta (hormiga esclava) ' +  str(n_ocurrencias) + ' veces observada </i>',tooltip=tooltip,
               icon=folium.Icon(color='cadetblue', icon='info-sign')
               )
        marker.add_to(specie1_map)

specie1_map.save('mapa1.html')
