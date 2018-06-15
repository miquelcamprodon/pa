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
import re


#resultsfolder = 'productos-industriales'


def parser_detail(resultsfolder):
    with open("pa_detail_output_{resultsfolder}.txt".format(resultsfolder=resultsfolder), 'wb') as fout:
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
        
        # For each url
        for filename in glob.glob('data/{resultsfolder}/getter_detail/*.html'.format(resultsfolder=resultsfolder)):
            print(filename)
            with open(filename, 'r') as f:
                myurl = f.readline()[0:-1]
                mydoc = etree.HTML(f.read())
                
                lres = mydoc.xpath("//div[@class='basicInfo']")
                for r in lres:
                    #print(etree.tostring(r))
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
                    myn = r.xpath("div[@class='container']//div[@class='titular']//h1")
                    #print("Company")
                    if (len(myn) > 0):
                        if myn[0].text is not None:
                            #print(myn[0].text)
                            dict_result['company'] = '' + myn[0].text
                    # Link-PA
                    dict_result['link-pa'] = myurl
                    #print(myurl)
                    # Category
                    myn = mydoc.xpath("//div[@class='bloque']//div[@class='box']//li")
                    #print("Category")
                    if (len(myn) > 0):
                        if myn[0].text is not None:
                            #print(myn[0].text)
                            dict_result['category'] = '' + myn[0].text
                    # Street address
                    myn = r.xpath("div[@class='container']//div[@class='adress']//span[@itemprop='streetAddress']")
                    #print("StreetAddress")
                    if (len(myn) > 0):
                        if myn[0].text is not None:
                            #print(myn[0].text)
                            dict_result['streetAddress'] = '' + myn[0].text
                    # Postal Code
                    myn = r.xpath("div[@class='container']//div[@class='adress']//span[@itemprop='postalCode']")
                    #print("PostalCode")
                    if (len(myn) > 0):
                        if myn[0].text is not None:
                            #print(myn[0].text)
                            dict_result['postalCode'] = '' + myn[0].text
                    # Address locality
                    myn = r.xpath("div[@class='container']//div[@class='adress']//span[@itemprop='addressLocality']")
                    #print("AddressLocality")
                    if (len(myn) > 0):
                        if myn[0].text is not None:
                            #print(myn[0].text)
                            dict_result['addressLocality'] = '' + myn[0].text
                    # Link
                    #myn = r.xpath("div[@class='container']//div[@class='adress']//a[@class='direccion']//span")
                    myn = r.xpath("div[@class='container']//div[@class='adress']//a[@class='direccion']/@title")
                    #print("Links")
                    #if (len(myn) > 0):
                    #    if myn[0].text is not None:
                    #        #print(myn[0].text)
                    #        dict_result['links'] = '' + myn[0].text
                    #print("Links")
                    if (len(myn) > 0):
                        if myn[0] is not None:
                            #print(myn[0].text)
                            dict_result['links'] = '' + myn[0].split('?')[0]
                    #print(dict_result['links'])
                    # Description
                    myn = mydoc.xpath("div[@class='row']//div[@class='links']//p")
                    #print("Description")
                    if (len(myn) > 0):
                        text = ''
                        for n in myn:
                            if n.text is not None:
                                #print(n.text)
                                text = text + n.text
                        dict_result['description'] = text
                    # Phone
                    myn = r.xpath("div[@class='container']//div[@class='telefono']//span[@itemprop='telephone']")
                    #print("Phone")
                    if (len(myn) > 0):
                        for n in myn:
                            if n.text is not None:
                                #print(n.text)
                                dict_result['phone'] = n.text
                    #print("")
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


#parser_detail(resultsfolder)
