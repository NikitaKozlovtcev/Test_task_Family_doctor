from app.db import database, weather_requests


async def post(city: str, country_code: str, timestamp: str, response: str):
    query = weather_requests.insert().values(country_code=country_code,
                                             city=city,
                                             date=timestamp,
                                             response=response,
                                             )
    return await database.execute(query=query)


async def get(country_code: str, city: str, date: str):
    query = weather_requests.select(). \
        where(country_code == weather_requests.c.country_code). \
        where(city == weather_requests.c.city). \
        where(date == weather_requests.c.date)

    return await database.fetch_one(query=query)
