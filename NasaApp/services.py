import os
import requests

def get_asteroids():
    #url = 'https://api.nasa.com/v2/nasa'
    #res = requests.get(url, headers={'Authorization':'Bearer %s' % 'access_token'})
    #resJson = res.json()
    asteroid_list = [{'name': 'alex', 'sizemin': '100', 'sizemax':'300', 'distance': '1000', 'nexttime': '2023-01-11', 'id': 'gdfgwdfcve'}]
    #for i in range(len(resJson['data'])):
    #    asteroid_list.append(resJson['data'][i])
    return asteroid_list
