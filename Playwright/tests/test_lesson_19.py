import requests
from config import *

'''
def test_get_single_user():
    req = requests.get(SINGLE_USER_URL, timeout=1)
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data']['id']) == 2, 'ID is incorrect'
    assert (r['data']['first_name']) == 'Janet', 'first_name is incorrect'
    assert (r['data']['last_name']) == 'Weaver', 'last_name is incorrect'


def test_get_list_users():
    req = requests.get(LIST_USERS_URL, timeout=1)
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data'][0]['id']) == 7, 'ID is incorrect'


def test_get_not_found_user():
    req = requests.get(NOT_FOUND_USER_URL, timeout=1)
    assert req.status_code == 404, 'Status code is incorrect'


def test_create_user():
    req = requests.post(CREATE_USER_URL, data = CREATE_USER_DATA)
    print(req.json())
    assert req.status_code == 201, 'Status code is incorrect'



print(test_get_single_user())
print(test_get_list_users())
print(test_get_not_found_user())
print(test_create_user())
'''

def test_get_single_user():
    req = requests.get(SINGLE_USER_URL)
    if req.status_code == 200:
        r = req.json()
        print(r)
        assert req.status_code == 200, 'Status code is incorrect'
        assert (r['data']['id']) == 2, 'ID is incorrect'
        assert (r['data']['first_name']) == 'Janet', 'first_name is incorrect'
        assert (r['data']['last_name']) == 'Weaver', 'last_name is incorrect'
    else:
        print(f'Ann error occurred with status code: {req.status_code}')


def test_get_list_users():
    req = requests.get(LIST_USERS_URL, timeout=1)
    r = req.json()
    print(r)
    assert req.status_code == 200, 'Status code is incorrect'
    assert (r['data'][0]['id']) == 7, 'ID is incorrect'


def test_get_not_found_user():
    req = requests.get(NOT_FOUND_USER_URL, timeout=1)
    assert req.status_code == 404, 'Status code is incorrect'


def test_create_user():
    req = requests.post(CREATE_USER_URL, data = CREATE_USER_DATA)
    print(req.json())
    assert req.status_code == 201, 'Status code is incorrect'