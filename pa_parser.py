#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#import subprocess
import requests
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import lxml
from lxml import etree
import glob
import csv


#resultsfolder = 'productos-industriales'
# output: "pa_output_{resultsfolder}.txt"

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



def parser(resultsfolder):
    with open("pa_output_{resultsfolder}.txt".format(resultsfolder=resultsfolder), 'wb') as fout:
        writer = csv.writer(fout, delimiter='\t')

        writer.writerow([
            'source',
            'company',
            'phone',
            'link-pa',
            'category',
            'streetAddress',
            'postalCode',
            'addressLocality',
            'links',
            'description'                        
        ])
        
        # For each category
        for p in lprovs:
            print(p)
            for filename in glob.glob('data/{resultsfolder}/getter/{resultsfolder}_{provincia}_*.html'.format(resultsfolder=resultsfolder, categoria=resultsfolder,provincia=p)):
                print(filename)
                print("{} {}".format(resultsfolder, p))
                with open(filename, 'r') as f:
                    
                    mydoc = etree.HTML(f.read())
                    lres = mydoc.xpath("//div[@class='central']//div[@class='box']")
                    for r in lres[1:]:
                        dict_result = {
                            'company':          '',
                            'phone':            '',
                            'link-pa':          '',
                            'category':         '',
                            'streetAddress':    '',
                            'postalCode':       '',
                            'addressLocality':  '',
                            'links':            '',
                            'description':      ''
                        }                                                            
                        
                        # Company
                        myn = r.xpath("div[@class='cabecera']//div[@class='row']//h2//span")
                        print("Company")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['company'] = myn[0].text
                        # Link-PA
                        myn = r.xpath("div[@class='cabecera']//a")
                        print("Link-PA")
                        if (len(myn) > 0):      
                            if 'href' in myn[0].attrib:
                                print(myn[0].attrib['href'])
                                dict_result['link-pa'] = myn[0].attrib['href']
                        # Category
                        myn = r.xpath("div[@class='row']//p[@class='categ']")
                        print("Category")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['category'] = myn[0].text
                        # Street address
                        myn = r.xpath("div[@class='row']//p[@class='location']//span[@itemprop='streetAddress']")
                        print("StreetAddress")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['streetAddress'] = myn[0].text
                        # Postal Code
                        myn = r.xpath("div[@class='row']//p[@class='location']//span[@itemprop='postalCode']")
                        print("PostalCode")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['postalCode'] = myn[0].text
                        # Address locality
                        myn = r.xpath("div[@class='row']//p[@class='location']//span[@itemprop='addressLocality']")
                        print("AddressLocality")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['addressLocality'] = myn[0].text
                        # Link
                        myn = r.xpath("div[@class='row']//div[@class='links']//span")
                        print("Links")
                        if (len(myn) > 0):
                            print(myn[0].text)
                            dict_result['links'] = myn[0].text
                        # Description
                        myn = r.xpath("div[@class='row']//div[@class='links']//p")
                        print("Description")
                        if (len(myn) > 0):
                            text = ''
                            for n in myn:
                                if n.text is not None:
                                    print(n.text)
                                    text = text + n.text
                            dict_result['description'] = text
                        # Phone
                        myn = r.xpath("div[@class='row']//div[@data-omniclick='phone']//a")
                        print("Phone")
                        #print(myn)
                        if (len(myn) > 0):
                            for n in myn:
                                if n.text is not None:
                                    print(n.text)
                                    dict_result['phone'] = n.text
                        print("")
                        writer.writerow([
                            filename,
                            dict_result['company'].encode('utf-8'), 
                            dict_result['phone'].encode('utf-8'),
                            dict_result['link-pa'].encode('utf-8'),
                            dict_result['category'].encode('utf-8'),
                            dict_result['streetAddress'].encode('utf-8'),
                            dict_result['postalCode'].encode('utf-8'),
                            dict_result['addressLocality'].encode('utf-8'),
                            dict_result['links'].encode('utf-8'),
                            dict_result['description'].encode('utf-8')
                            ])


#parser(resultsfolder)
