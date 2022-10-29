import json
import requests
import os
import libs.cache as cache

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    ...


def getREST(url: str, params: dict = {}):

    key = f'GITHUB - {url}{params}'
    che = cache.get_cache(key)
    if che != None:
        return che

    print(url)

    request = requests.get(url,params=params,headers={
        'authorization': f'token {os.getenv("API_TOKEN")}'
    })

    if request.status_code == 404:
        return None

    if request:
        data = request.json()
        cache.store_cache(key,data)
        return data
    print(request.text)

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
