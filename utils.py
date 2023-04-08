#Utility functions

import urllib.request
import python_weather
import asyncio
import os

def NetworkUp():
    try:
        urllib.request.urlopen("http://google.com")
        return True
    except:
        return False

async def GetWeatherTemp():
    async with python_weather.Client(format=python_weather.METRIC) as client:
        weather = await client.get("Baldivis")
        return weather.current.temperature