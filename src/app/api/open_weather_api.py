import os

import aiohttp

URL_base = 'https://api.openweathermap.org'
API_KEY = os.getenv("API_KEY")


async def get(city, country_code, timestamp):
    url_city = f'{URL_base}/geo/1.0/direct?q={city},{country_code}&limit={10}&appid={API_KEY}'
    coordinates = await openweathermap_request(url_city)
    if coordinates:
        lat = coordinates[0]['lat']
        lon = coordinates[0]['lon']
        url_weather = f'{URL_base}/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={int(timestamp)}&appid={API_KEY}'
        wthr = await openweathermap_request(url_weather)
        return wthr
    else:
        return False


async def openweathermap_request(URL):
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as resp:
            resp_status = resp.status
            if resp_status == 200:
                response = await resp.json()
                return response
            else:
                return False
