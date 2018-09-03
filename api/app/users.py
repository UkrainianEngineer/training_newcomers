import requests

from flask import current_app

def get_users():
    """
    Returns list of all users to GET request.
    """
    users_list = current_app.config["context"]["users_manager"].get_all_users()
    return {"users": users_list}, requests.codes.ok

def add_user(user_data):
    """
    This method is using to add a new user.
    This is realized via POST request.
    """
    name = user_data.get("name")
    surname = user_data.get("surname")
    age = user_data.get("age")
    if not name:
        return {"message": "missing user's name"}, requests.codes.bad_request

    if not surname:
        return {"message": "missing user's surname"}, requests.codes.bad_request

    if not age:
        return {"message": "missing user's age"}, requests.codes.bad_request

    # TODO: think about context management or something similar.
    user = current_app.config["context"]["users_manager"].add_user(
        name=name,
        surname=surname,
        age=age
    )

def get_user(user_id):
    user = current_app.config["context"]["users_manager"].fetch_user(user_id)
    return {"user": user}, requests.codes.ok

def remove_user(user_id):
    user = current_app.config["context"]["users_manager"].remove_user(user_id)
    return {"user_id": user_id}, requests.codes.ok

"""
def update_user(user_data):
    user = current_app.config["context"]["users_manager"].update_user(user_data)
    return {"user_id": user_id}, requests.codes.ok
"""
