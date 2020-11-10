import requests
# https://api.maas2.apollorion.com/


def get_latest_response():
    x = requests.get('https://api.maas2.apollorion.com/')
    return x


def get_latest_response_code():
    return get_latest_response().status_code


def get_latest_json():
    return get_latest_response().json()


def get_specific_sol(this_sol):
    url = 'https://api.maas2.apollorion.com/{0}'.format(str(this_sol))
    specific_sol = requests.get(url).text
    return specific_sol
