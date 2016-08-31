#!/usr/bin/python
# -*- coding: utf-8 -*-

###################################################################################
# Se pasa como argumento la url de un playlist de youtube y este devolverá en un archivo (playlist.txt) cada URL
# Autor: Emanuel Malfatti 
# E-mail: ejmalfatti@outlook.com
# GitHub: https://ejmalfatti.github.io
# Licencia: GPLv3
###################################################################################

import requests
from bs4 import BeautifulSoup
import os
import sys


urlYB = sys.argv[1]

r  = requests.get(urlYB)
data = r.text
soup = BeautifulSoup(data, 'lxml')
i = 0
lista = []

for item in soup.find_all(attrs={'class': 'pl-video-thumbnail'}):
	for link in item.find_all('a'):
		listaLink = open('playlists.txt','w')
		URL = "https://www.youtube.com" + link.get('href')
		lista.append(URL+"\n")
		listaLink.writelines(lista)
		#print "https://www.youtube.com" + link.get('href')
		i += 1
lista = []
VIDEOS = "\nLa cantidad de videos para descargar son: " + str(i)
lista.append(VIDEOS+"\n")
listaLink.writelines(lista)
listaLink.close()
