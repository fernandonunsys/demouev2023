# -*- coding: utf-8 -*-
"""
Created on Tue Dic 1 22:15:05 2021

"""


import datetime
import time
import random
import requests

iotagenturl = 'http://localhost:7896/iot/d'
iotagentkey = '4jggokgpepnvsb2uv4s40d5911'


i=0

while i<=10:

 
    devicename1 ="Prensa1" 
    devicename2 ="Prensa2"
    #devicename2 ="Product011"



    url = iotagenturl+"?i="
    #http://localhost:7896/iot/d?i=Product010&k=4jggokgpepnvsb2uv4s40d5911
    endpoint1 = url+devicename1+"&k="+iotagentkey
    endpoint2 = url+devicename2+"&k="+iotagentkey
    header = {"ContentType":"text/plain"} 


    ahora = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    Yield = random.uniform(5, 100)
    Scrap = random.uniform(1, 50)
    Ok = random.uniform(1, 50)
    payload1 = "Yield|"+str('{0:.2f}'.format(Yield))+"|Scrap|"+str("{0:.2f}".format(Scrap))+"|Ok|"+str("{0:.2f}".format(Ok))+"|d|"+str(ahora)
    
    payload2= "Yield|"+str('{0:.2f}'.format(Yield))+"|Scrap|"+str("{0:.2f}".format(Scrap))+"|Ok|"+str("{0:.2f}".format(Ok))+"|d|"+str(ahora)
    
    r1 = requests.post(url= endpoint1,headers=header, data=payload1)
    print("datos sensor {} {} ".format(devicename1,payload1))
    time.sleep(1)
    
    r2 = requests.post(url= endpoint2,headers=header, data=payload1)
    print("datos sensor {} {} ".format(devicename2,payload2))
    time.sleep(1)

    i+=1







