import logging

import connexion

from users_manager import UsersManager

class HTTPAPI(object):

    def __init__(self):
        self.__app = connexion.App(__name__, swagger_json=False)
        self.__app.add_api("api.yaml")
        self.__app.app.config["context"] = {}
        self.__app.app.config["context"]["users_manager"] = UsersManager()

        self.__app.app.logger.disabled = False
        logging.getLogger("werkzeug").disabled = False

    def __call__(self):
        self.__app.run(port=5000, threaded=True)
