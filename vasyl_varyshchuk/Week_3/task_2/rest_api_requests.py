"""
This script contains functions for display, create, update and delete users from server with REST API
"""
import requests
import json

URL = 'http://127.0.0.1:5000/api/'
headers = {'Content-type': 'application/json'}


def catch_response_exceptions(func):
    """A decorator that wraps the passed in functions and catches
    requests exceptions which can occur"""
    def wrapper(*args):
        try:
            return func(*args)
        except requests.exceptions.ConnectionError as error:
            print('Connection error:', error.message)
        except requests.exceptions.HTTPError as error:
            print('HTTP error:', error.message)
        except requests.exceptions.InvalidSchema as error:
            print('Invalid Schema error:', error.message)
        except requests.exceptions.Timeout as error:
            print('Timeout error:', error.message)
        except requests.exceptions.RequestException as error:
            print('Unexpected error:', error.message)
    return wrapper


@catch_response_exceptions
def get_list_of_users():
    """This function returns list of users from a server"""
    response = requests.get(URL+'users/', timeout=10)
    response.raise_for_status()
    return response.json()['users']


@catch_response_exceptions
def get_concrete_user(user_id):
    """This function gets information about concrete user from server by user_id"""
    response = requests.get(URL+'users/{}/'.format(user_id), timeout=5)
    response.raise_for_status()
    return response.json()['user']


@catch_response_exceptions
def add_new_user(new_user_info):
    """
    This function adds new user to the server passing a dictionary of information about user.
    new_user_info parameter should be passed in the following format:
        {'name': 'user_name', 'surname': 'user_surname', 'age': user_age}
    """
    new_user_json = json.dumps(new_user_info)
    response = requests.post(URL+'users/', data=new_user_json, headers=headers, timeout=5)
    response.raise_for_status()
    print('New user was successfully added')


@catch_response_exceptions
def update_user_info(user_id, update_info):
    """
    This function updates information about current user.
    update_info -  dictionary with new information about user
    """
    if get_concrete_user(user_id) is not None:
        update_info_json = json.dumps(update_info)
        response = requests.put(URL+'users/{}/'.format(user_id), data=update_info_json, headers=headers, timeout=5)
        response.raise_for_status()
        print('Information was updated for user with id={}'.format(user_id))
    else:
        print('User with id={} does not exist'.format(user_id))


@catch_response_exceptions
def delete_user(user_id):
    """This function deletes user from server passing user id"""
    if get_concrete_user(user_id) is not None:
        response = requests.delete(URL+'users/{}/'.format(user_id), timeout=5)
        response.raise_for_status()
        print('User with id={} was deleted'.format(user_id))
    else:
        print('User with id={} does not exist'.format(user_id))


# get all users from server
print(get_list_of_users())

# get information about concrete user
print(get_concrete_user(2))

# add new user to the server
new_user = {'name': 'Vasyl', 'surname': 'Varyshchuk', 'age': 28}
add_new_user(new_user)

# update an existing user information
updated_user_info = {'age': 29}
update_user_info(2, updated_user_info)

# delete an existing user
delete_user(3)
