import herepy
import json
import numpy as np
import pandas as pd
import requests
import xml
def here():
 geocoderApi = herepy.GeocoderApi('')
 place1=input("Enter your current position please:")
 place2=input("Enter your destination please:")
 if input == "":
   print('wainting')
 else:

    response1 = geocoderApi.free_form(place1)
    response2 = geocoderApi.free_form(place2)
    dict1 = response1.as_dict()
    dict2 = response2.as_dict()
 #print(dict)

    Latitude1 = dict1['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    Longitude1 = dict1['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    Latitude2 = dict2['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
    Longitude2 = dict2['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']
    print(dict1)
    print(Latitude2)
    if Longitude2 == "":
       print('waiting')
    else:
        routingApi = herepy.RoutingApi('', '')
        response3 = routingApi.public_transport([Latitude1, Longitude1],
                                        [Latitude2, Longitude2],
                                                True,
                                                [herepy.RouteMode.publicTransport, herepy.RouteMode.fastest])
        print(response3)
        dict3 = response3.as_dict()
        Indicazioni = dict3['Response']['Route'][0]['leg'][0]['maneuver'][0]['Instruction']
