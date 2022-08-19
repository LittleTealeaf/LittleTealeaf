import requests
import os
from dotenv import load_dotenv
import libs.cache as cache
import time


load_dotenv()


def getData(endpoint: str, params: dict = {}):

    key = f"WAKATIME - {endpoint}{params}"
#     che = cache.get_cache(key)
#     if che != None:
#         return che
    params = params.copy()
    params['api_key'] = os.getenv("WAKA_TOKEN")

    url = f"https://www.wakatime.com{endpoint}"
    response = requests.get(
        url,
        params=params,
    )
    print(endpoint)

    if response:
        data = response.json()

        cache.store_cache(key, data)
        return data
    print(response.text)

def getStats(timeFrame: str):
    key = f"WAKATIME/STATS/{timeFrame}"
    che = cache.get_cache(key)
    if che != None:
        return che
    params = {
        'api_key': os.getenv('WAKA_TOKEN')
    }

    stats = None
    attempts = 0
    while not stats and attempts < 10:
        attempts = attempts + 1
        print(f"Fetching stats for {timeFrame}")
        response = requests.get(f'https://www.wakatime.com/api/v1/users/current/stats/{timeFrame}',params=params)
        data = response.json()["data"]
        if data["is_up_to_date"] and data["status"] == "ok":
            stats = data
            break
        print(f"Waiting 3 minutes before attempting again")
        time.sleep(180)
    if stats:
        cache.store_cache(key,stats)
    return stats
