""""
This script contains functions for display, create, update and delete users from server with REST API
"""
import requests
import json

url = 'http://127.0.0.1:5000/api/users/'
headers = {'Content-type': 'application/json'}


def get_list_of_users():
    """This function returns list of users from a server"""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['users']
    else:
        print('Something went wrong', response.text)
    print('------------------------------------------')


def get_concrete_user(user_id):
    """This function gets information about concrete user from server by user_id"""
    response = requests.get('http://127.0.0.1:5000/api/users/{}/'.format(user_id))
    if response.status_code == 200:
        if response.json()['user'] is not None:
            return response.json()
        else:
            print('User with id={} does not exist'.format(user_id))
            print('------------------------------------------')
    else:
        print('Something went wrong with response from server.', response.status_code, response.text)
        print('------------------------------------------')


def add_new_user(new_user_info):
    """
    This function adds new user to the server passing a dictionary of information about user.
    new_user_info parameter should be passed in the following format:
        {'name': 'user_name', 'surname': 'user_surname', 'age': user_age}
    """
    new_user_json = json.dumps(new_user_info)
    response = requests.post(url, data=new_user_json, headers=headers)
    if response.status_code == 200:
        print('New user was successfully added.')
    else:
        print('Something went wrong with response from server.', response.status_code, response.text)
    print('------------------------------------------')


def update_user_info(user_id, update_info):
    """
    This function updates information about current user.
    update_info -  dictionary with new information about user
    """
    if get_concrete_user(user_id) is not None:
        url = 'http://127.0.0.1:5000/api/users/{}/'.format(user_id)
        update_info_json = json.dumps(update_info)
        response = requests.put(url, data=update_info_json, headers=headers)
        if response.status_code == 200:
            print('Information was updated for user with id={}'.format(user_id))
        else:
            print('Something went wrong.', response.status_code, response.text)
        print('------------------------------------------')


def delete_user(user_id):
    """This function deletes user from server passing user id"""
    if get_concrete_user(user_id) is not None:
        response = requests.delete('http://127.0.0.1:5000/api/users/{}/'.format(user_id))
        if response.status_code == 200:
            print('User with id={} was deleted'.format(user_id))
        else:
            print('Something went wrong.', response.status_code, response.text)
        print('------------------------------------------')


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

