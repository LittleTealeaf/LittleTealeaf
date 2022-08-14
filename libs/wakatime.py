import requests
import os
from dotenv import load_dotenv
import libs.cache as cache
import base64


load_dotenv()


def getData(endpoint: str, params: dict = {}):

    key = f"WAKATIME - {endpoint}{params}"
    che = cache.get_cache(key)
    if che != None:
        return che
    params = params.copy()

    url = f"https://www.wakatime.com{endpoint}"
    response = requests.get(
        url,
        params=params,
        headers={
            "Authorization": f'Basic {base64.b64encode(os.getenv("WAKA_TOKEN").encode("ascii"))}'
        },
    )
    print(endpoint)

    if response:
        data = response.json()

        cache.store_cache(key, data)
        return data
    print(response.text)
