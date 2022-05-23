import json
import requests
import os
from dotenv import load_dotenv
import libs.cache as cache

load_dotenv()


def getREST(url: str, params: dict = {}):
    key = f'{url}{params}'
    che = cache.get_cache(key)
    if che != None:
        return che

    request = requests.get(url,params=params,headers={
        'authorization': f'token {os.getenv("API_TOKEN")}'
    })
    if request:
        data = request.json()
        cache.store_cache(key,data)
        return data

def getGraphQL(query: dict):
    che = cache.get_cache(query)
    if che != None:
        return che

    request = requests.post('https://api.github.com/graphql',json={'query': query},headers={
        'authorization': f'token {os.getenv("API_TOKEN")}'
    })
    if request.status_code == 200:
        cache.store_cache(query,request.json())
        return request.json()
    else:
        raise Exception("Query failed: " + str(request.status_code))
