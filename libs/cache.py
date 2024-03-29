import json
import os
from random import Random
from time import time


VERSION = '1'
DEFAULT_TIME = 6
MIN_TIME = 1
MAX_TIME = 24

VALID_FILE_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg\
                        hijklmnopqrstuvwxyz1234567890_'


def get_file(key):
    seed = f'{VERSION}{key}'
    random = Random(seed)
    fileName = "".join(random.choices(VALID_FILE_CHARACTERS, k=10)) + ".json"
    return os.path.join('.', '.cache', fileName)


def store_cache(key, value, no_delete=False):
    cache = {
        'value': value,
        'expires': time() + 60 * 60 * DEFAULT_TIME,
        'duration': 60 * 60 * DEFAULT_TIME
    }

    fileName = get_file(key)

    if os.path.exists(fileName):
        with open(fileName) as f:
            old_cache = json.load(f)

            if json.dumps(value) == json.dumps(old_cache['value']):
                cache['duration'] = min(MAX_TIME, old_cache['duration'] * 1.5)
            else:
                cache['duration'] = max(MIN_TIME, old_cache['duration'] / 2)
            cache['expires'] = time() + 60 * 60 * cache['duration']

    cache['no_delete'] = no_delete

    os.makedirs(os.path.join('.', '.cache'), exist_ok=True)
    with open(fileName, 'w') as f:
        f.write(json.dumps(cache))


def get_cache(key, no_delete=False):
    fileName = get_file(key)

    if not os.path.exists(fileName):
        return None

    with open(fileName) as f:
        data = json.load(f)

        if not no_delete and data['expires'] < time():
            return None

        return data['value']


def clean_cache():
    "Cycles through all cached items and removes any files that are expired"
    CUTOFF_DATE = time() - 60 * 60 * DEFAULT_TIME
    if os.path.exists(os.path.join('.', '.cache')):
        for file in os.listdir(os.path.join('.', '.cache')):
            mark_delete = False
            with open(os.path.join('.', '.cache', file)) as f:
                cache = json.load(f)
                if not cache['no_delete'] and cache['expires'] < CUTOFF_DATE:
                    mark_delete = True
                if mark_delete:
                    os.remove(os.path.join('.', '.cache', file))
