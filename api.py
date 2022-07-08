import requests
# https://gorest.co.in


def api_post():
    url = "https://gorest.co.in"
    access_token = "5fbbcdae357a0e5c64ccd005ebb3adf5b6ea5436b5c8909140dfa2007821b5e9"
    payload = '{"name":"Kermit D Frog","salary":"123","age":"23"}'
    x = requests.post(url, data=payload)
    print(x.text)
    print(x.headers)
    print(x.status_code)
    print(x.request)
    return x.status_code


def api_get_status_code():
    url = "https://gorest.co.in/public/v2/users"
    x = requests.get(url)
    return x.status_code
