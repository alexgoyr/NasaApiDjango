import os
import requests
from datetime import datetime, timedelta

API_KEY = "eyyeOtiD9ZHkjJcrZoiM2i6WqjEwJDPdLTEgJFcT"

def get_asteroids(start, end):
    startDate = datetime.strptime(start, "%Y-%m-%d")
    EndDate = datetime.strptime(end, "%Y-%m-%d")
    url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date='+start+'&end_date='+end+'&detailed=true&api_key='+API_KEY
    res = requests.get(url)
    if res.status_code != 200:
        return []
    resJson = res.json()
    asteroid_list = []
    currentDate = startDate
    while currentDate != EndDate + timedelta(days=1):
        for asteroid in resJson['near_earth_objects'][currentDate.strftime("%Y-%m-%d")]:
            tempAsteroid = {}
            tempAsteroid['name'] = asteroid['name']
            tempAsteroid['sizemin'] = asteroid['estimated_diameter']["kilometers"]["estimated_diameter_min"]
            tempAsteroid['sizemax'] = asteroid['estimated_diameter']["kilometers"]["estimated_diameter_max"]
            tempAsteroid['distance'] = asteroid['close_approach_data'][0]["miss_distance"]["lunar"]
            tempAsteroid['id'] = asteroid['id']
            tempAsteroid['nexttime'] = "Unknown"
            asteroid_list.append(tempAsteroid)
        currentDate = currentDate + timedelta(days=1)
    return asteroid_list

def get_asteroidDetails(id):
    url = 'https://api.nasa.gov/neo/rest/v1/neo/'+id+'?api_key='+API_KEY
    res = requests.get(url)
    if res.status_code != 200:
        return []
    resJson = res.json()
    previousCloseApproach = []
    i = 0
    closeApproach = resJson['close_approach_data']
    while i < len(closeApproach):
        today = datetime.today()
        close_approach_date = datetime.strptime(closeApproach[i]['close_approach_date'], "%Y-%m-%d")
        if close_approach_date > today:
            i = i - 1
            break
        i = i + 1
    j = 0
    while i > 0 and j < 5:
        tempCloseApproach = {
            'date' : closeApproach[i]['close_approach_date'],
            'distance': closeApproach[i]['miss_distance']['lunar']
        }
        previousCloseApproach.append(tempCloseApproach)
        i = i - 1
        j = j + 1

    return previousCloseApproach