import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.api import crud_weather
from app.api.open_weather_api import get

router = APIRouter()

log = logging.getLogger(__name__)

@router.get("/weather", name='Get wheather by city with region and time')
async def main_get_weather(country_code: Optional[str] = Query(..., min_length=2, max_length=3),
                           city: Optional[str] = Query(..., min_length=3, max_length=50),
                           date: Optional[str] = Query(..., min_length=2, max_length=50)):
    try:
        date = datetime.fromisoformat(date)
        timestamp = str(int(datetime.timestamp(date)))
    except ValueError:
        raise HTTPException(status_code=400, detail="Wrong date time format")
    else:
        exist = await crud_weather.get(country_code, city, timestamp)

    if exist:
        log.info(f'cache: {exist}')
        return exist
    else:
        weather = await get(city, country_code, timestamp)
        if weather:
            weather_request_id = await crud_weather.post(city, country_code, timestamp, str(weather['current']))
            response_object = {
                "id": weather_request_id,
                "country_code": country_code,
                "city": city,
                "date": date,
                "response": weather['current'],
            }
            log.info(f'new: {response_object}')
            return response_object
        else:
            raise HTTPException(status_code=200, detail="Weather not found")
