import requests
# https://api.maas2.apollorion.com/


def get_latest_response():
    return requests.get('https://api.maas2.apollorion.com/')


def get_status_code():
    return get_latest_response().status_code


def get_latest_json():
    return get_latest_response().json()


def get_specific_sol(this_sol):
    url = f'https://api.maas2.apollorion.com/{str(this_sol)}'
    return requests.get(url).text
