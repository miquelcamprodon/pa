#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import re
#import subprocess
import requests
from HTMLParser import HTMLParser

# https://www.paginasamarillas.es/all__.html
#resultsfolder = 'productos-industriales'

# output: "data/{resultsfolder}/getter/{categoria}_{provincia}_{pagina}.html

lprovs = [
'a-coruña',     'alava',        'albacete',     'alicante',     'almeria',
'asturias',     'avila',        'badajoz',      'baleares',     'barcelona',
'burgos',       'caceres',      'cadiz',        'cantabria',    'castellon',
'ceuta',        'ciudad-real',  'cordoba',      'cuenca',       'girona',
'granada',      'guadalajara',  'guipuzcoa',    'huelva',       'huesca',
'jaen',         'la-rioja',     'las-palmas',   'leon',         'lleida',
'lugo',         'madrid',       'malaga',       'melilla',      'murcia',
'navarra',      'ourense',      'palencia',     'pontevedra',   'salamanca',
'segovia',      'sevilla',      'soria',        'tarragona',    'tenerife',
'teruel',       'toledo',       'valencia',     'valladolid',   'vizcaya',
'zamora',       'zaragoza'
]


class MyNewHTMLParser(HTMLParser):
    total_results = 0
    
    def handle_data(self, data):
        try:
            if 'resultados' in data:
                print("Data     :", data)
                print(data.split(' ')[0][1:])
                self.total_results = int(re.sub('\.','',data.split(' ')[0][1:]))
        except:
            self.total_results = 0

def getter(resultsfolder):
    # For each province
    for p in lprovs:   
        print(p) 
        r = requests.get("https://www.paginasamarillas.es/a/{categoria}/{provincia}/".format(categoria=resultsfolder, provincia=p))
        r.text
        myparser = MyNewHTMLParser()
        myparser.feed(r.text)
        total_prov = myparser.total_results
        
        with open("data/{resultsfolder}/getter/{categoria}_{provincia}_1.html".format(resultsfolder=resultsfolder, categoria=resultsfolder, provincia=p), "w") as f: 
            f.write(r.text.encode('utf-8')) 
        #subprocess.call(["wget","https://www.paginasamarillas.es/a/{categoria}/{provincia}/".format(categoria=category, provincia=p),"-O", "getter/{categoria}_{provincia}_1.html".format(categoria=category, provincia=p)])
        time.sleep(0.5)
        total_prov_15 = int((total_prov + 14)/ 15.0) 
        
        for i in range(2, total_prov_15 + 1):
            print("{} de {}").format(i, total_prov_15)
            r = requests.get("https://www.paginasamarillas.es/a/{categoria}/{provincia}/{pagina}".format(categoria=resultsfolder, provincia=p, pagina=str(i)))
            r.text
            with open("data/{resultsfolder}/getter/{categoria}_{provincia}_{pagina}.html".format(resultsfolder=resultsfolder, categoria=resultsfolder, provincia=p, pagina=str(i)), "w") as f: 
                f.write(r.text.encode('utf-8')) 
            #subprocess.call(["wget","https://www.paginasamarillas.es/a/{categoria}/{provincia}/{pagina}".format(categoria=category, provincia=p, pagina=str(i)),"-O", "getter/{categoria}_{provincia}_{pagina}.html".format(categoria=category, provincia=p, pagina=str(i))])
            time.sleep(0.5)


#getter(resultsfolder)
