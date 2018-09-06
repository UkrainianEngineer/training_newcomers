"""
This script contains functions for display, create, update and delete users from server with REST API
"""
import requests
import json

URL = 'http://127.0.0.1:5000/api/'
headers = {'Content-type': 'application/json'}


def get_list_of_users():
    """This function returns list of users from a server"""
    try:
        response = requests.get(URL+'users/')
        response.raise_for_status()
        return response.json()['users']
    except requests.RequestException as error:
        print(error)


def get_concrete_user(user_id):
    """This function gets information about concrete user from server by user_id"""
    try:
        response = requests.get(URL+'users/{}/'.format(user_id))
        response.raise_for_status()
        return response.json()['user']
    except requests.RequestException as error:
        print (error)


def add_new_user(new_user_info):
    """
    This function adds new user to the server passing a dictionary of information about user.
    new_user_info parameter should be passed in the following format:
        {'name': 'user_name', 'surname': 'user_surname', 'age': user_age}
    """
    new_user_json = json.dumps(new_user_info)
    try:
        response = requests.post(URL+'users/', data=new_user_json, headers=headers)
        response.raise_for_status()
        print('New user was successfully added')
    except requests.RequestException as error:
        print(error)


def update_user_info(user_id, update_info):
    """
    This function updates information about current user.
    update_info -  dictionary with new information about user
    """
    update_info_json = json.dumps(update_info)
    user_url = URL + 'users/{}/'.format(user_id)
    try:
        get_user_response = requests.get(user_url)
        put_response = requests.put(user_url, data=update_info_json, headers=headers)
        put_response.raise_for_status()
        if get_user_response.json()['user'] is not None:
            print('Information was updated for user with id={}'.format(user_id))
        else:
            print('User with id={} does not exist'.format(user_id))
    except requests.RequestException as error:
        print(error)


def delete_user(user_id):
    """This function deletes user from server passing user id"""
    user_url = URL+'users/{}/'.format(user_id)
    try:
        get_user_response = requests.get(user_url)
        delete_response = requests.delete(user_url)
        delete_response.raise_for_status()
        if get_user_response.json()['user'] is not None:
            print('User with id={} was deleted'.format(user_id))
        else:
            print('User with id={} does not exist'.format(user_id))
    except requests.RequestException as error:
        print(error)


# get all users from server
print(get_list_of_users())

# get information about concrete user
print(get_concrete_user(5))

# add new user to the server
new_user = {'name': 'Vasyl', 'surname': 'Varyshchuk', 'age': 28}
add_new_user(new_user)

# update an existing user information
updated_user_info = {'age': 29}
update_user_info(2, updated_user_info)

# delete an existing user
delete_user(3)
