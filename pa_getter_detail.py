#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
#import subprocess
import requests
from HTMLParser import HTMLParser
import re
import datetime


# input
#resultsfolder = 'productos-industriales'
# output data/{resultsfolder}/getter_detail/{myurl}

def getter_detail(resultsfolder):
    #with open('urls_detail_{}.txt'.format(resultsfolder), 'rb') as fin:        

    with open('pa_output_{}.txt'.format(resultsfolder), 'rb') as fin:         
        for i,myline in enumerate(fin):
            if i > 0: # avoid first line
                try:
                    myurl = myline[0:-1].split('\t')[3]
                    print("{} - {} - {}".format(datetime.datetime.now(), i, myurl))

                    r = requests.get(myurl)

                    with open("data/{resultsfolder}/getter_detail/{myurl}".format(resultsfolder=resultsfolder, myurl=re.sub('/','_',myurl)), "w") as fout: 
                        fout.write(myurl)
                        fout.write('\n')
                        fout.write(r.text.encode('utf-8')) 
                except:
                    pass

            time.sleep(0.5) 
                
            
#getter_detail(resultsfolder)
