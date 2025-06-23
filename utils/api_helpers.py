import requests
from utils.config import CONFIG

def get_all_charity(headers):
    endpoint = 'api/charity/getAll'
    params = {
        'page' : 1,
        'limit' : 10,
        'isPending' : True,
        'countryId' : 5
    }
    response = requests.get(url = CONFIG['api_base'] + endpoint, params = params, headers=headers)
    return response

def get_all_club(headers):
    endpoint = 'api/club/getAll'
    params = {
        'page' : 1,
        'limit' : 10,
        'isPending' : True,
        'countryId' : 5
    }
    response = requests.get(url = CONFIG['api_base'] + endpoint, params=params, headers=headers)
    return response
