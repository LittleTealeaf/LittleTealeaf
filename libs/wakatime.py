import requests
import os
from dotenv import load_dotenv
import libs.cache as cache


load_dotenv()

def getData(endpoint: str, params: dict = {}):

    key =f'WAKATIME - {endpoint}{params}'
    che = cache.get_cache(key)
    if che != None:
        return che

        print

    params = params.copy()
    params['api_key'] = os.getenv('WAKA_TOKEN')

    url = f'https://www.wakatime.com{endpoint}'
    response = requests.get(url,params=params)
    print(endpoint)

    if response:
        data = response.json()

        cache.store_cache(key,data)
        return data
