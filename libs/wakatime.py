import requests
import os
from dotenv import load_dotenv
import libs.cache as cache
import time

load_dotenv()


def getData(endpoint: str, params: dict = {}):
    key = f'WAKATIME - {endpoint}{params}'
    che = cache.get_cache(key)
    if che is not None:
        return che

    params = params.copy()
    params['api_key'] = os.getenv('WAKATIME_TOKEN')

    url = f"https://www.wakatime.com/{endpoint}"
    response = requests.get(url, params=params)
    print(endpoint)

    if response:
        data = response.json()
        cache.store_cache(key, data)
        return data


def getStats(timeFrame: str):
    key = f"WAKATIME/STATS/{timeFrame}"

    params = {
        'api_key': os.getenv('WAKATIME_TOKEN')
    }

    stats = None
    attempts = 0

    while not stats and attempts < 10:
        attempts = attempts + 1
        print(f"Fetching Stats for {timeFrame}")
        response = requests.get(
            f"https://www.wakatime.com/api/v1/users/current/stats/{timeFrame}",
            params=params
        )

        json_response = response.json()
        if 'data' not in json_response:
            print("Got Value: ", json_response)
            return None
        data = json_response['data']

        if data["is_up_to_date"] and data["status"] == "ok":
            stats = data
            break
        print("Waiting 3 minutes before attempting again")
        time.sleep(180)
    if stats:
        cache.store_cache(key, stats, no_delete=True)
    else:
        stats = cache.get_cache(key, no_delete=True)
    return stats
