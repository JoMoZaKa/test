import requests
# from enums.global_enums import Error

'''
def get_request():
    req = requests.get('https://reqres.in/api/users/2')
    assert req.status_code == 200
    return req

print(get_request()) 

def get_single_user():
    req = requests.get('https://reqres.in/api/users/2')
    assert req.status_code == 200
    return req

def get_list_users():
    req = requests.get('https://reqres.in/api/users?page=2')
    assert req.status_code == 200
    return req

def get_not_found_user():
    req = requests.get('https://reqres.in/api/users/267')
    assert req.status_code == 404
    return req

print(get_single_user())
print(get_list_users())
print(get_not_found_user())



def get_single_user():
    req = requests.get('https://reqres.in/api/users/2')
    assert req.status_code == 200, Error.status_code
    return req

def get_list_users():
    req = requests.get('https://reqres.in/api/users?page=2')
    assert req.status_code == 200, Error.status_code
    return req

def get_not_found_user():
    req = requests.get('https://reqres.in/api/users/267')
    assert req.status_code == 404, Error.status_code
    return req

print(get_single_user())
print(get_list_users())
print(get_not_found_user())


def get_single_user():
    req = requests.get('https://reqres.in/api/users/2')
    assert req.status_code == 200, 'Status code is incorrect'
    return req

def get_list_users():
    req = requests.get('https://reqres.in/api/users?page=2')
    assert req.status_code == 200, 'Status code is incorrect'
    return req

def get_not_found_user():
    req = requests.get('https://reqres.in/api/users/267')
    assert req.status_code == 404, 'Status code is incorrect'
    return req

print(get_single_user())
print(get_list_users())
print(get_not_found_user())


def get_single_user():
    req = requests.get('https://reqres.in/api/users/2')
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data']['id']) == 2, 'ID is incorrect'
    return req

def get_list_users():
    req = requests.get('https://reqres.in/api/users?page=2')
    assert req.status_code == 200, 'Status code is incorrect'
    return req

def get_not_found_user():
    req = requests.get('https://reqres.in/api/users/267')
    assert req.status_code == 404, 'Status code is incorrect'
    return req

print(get_single_user())
print(get_list_users())
print(get_not_found_user())


def get_single_user():
    req = requests.get('https://reqres.in/api/users/2', timeout=1)
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data']['id']) == 2, 'ID is incorrect'
    assert (r['data']['first_name']) == 'Janet', 'first_name is incorrect'
    assert (r['data']['last_name']) == 'Weaver', 'last_name is incorrect'
    return req

def get_list_users():
    req = requests.get('https://reqres.in/api/users?page=2', timeout=1)
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data'][0]['id']) == 7, 'ID is incorrect'
    return req

def get_not_found_user():
    req = requests.get('https://reqres.in/api/users/267', timeout=1)
    assert req.status_code == 404, 'Status code is incorrect'
    return req

print(get_single_user())
print(get_list_users())
print(get_not_found_user())

'''

def create_user():
    params_create_user = {
        "name": 'JoJo',
        "job": 'toaster'
    }
    req = requests.post('https://reqres.in/api/users', data = params_create_user)
    print(req.json())
    assert req.status_code == 201, 'Status code is incorrect'
    return req

print(create_user())
