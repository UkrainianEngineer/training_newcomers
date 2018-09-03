===================================================================
This module contains Python code for basic REST API service.
REST API is based on `connexion` library.
===================================================================

To use all dependencies for this API please use virtual environment.

1. Install virtual environment

    For more details read:

        https://askubuntu.com/a/244642

2. Activate your virtual environment. E.g.:

    source venv/bin/activate

3. Install all required dependencies:

    pip install -r requirements.txt

4. Run the API server:

    python api.py

Your API is ready to receive requests.

Test your API:

    curl -X GET http://127.0.0.1:5000/api/users/

It should return empty list of users.
