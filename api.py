import requests
# http://dummy.restapiexample.com/


def api_post():
    url = "http://dummy.restapiexample.com/create/"
    payload = '{"name":"Kermit D Frog","salary":"123","age":"23"}'
    x = requests.post(url, data=payload)
    # print(x.text)
    # print(x.headers)
    # print(x.status_code)
    # print(x.request)
    return x.status_code


def api_get():
    url = "http://dummy.restapiexample.com/employee/1"
    x = requests.get(url)
    return x.status_code
