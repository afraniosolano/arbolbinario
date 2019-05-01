""" Import packages """
import json
import logging
from typing import Dict
from flask import abort, make_response, jsonify
from connexion import request
import jsonpickle
from rest import app
import exception.exception as exception

class ArbolResource():
    """ class ArbolResource """

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    # pylint: disable=W0703
    def save_arbol(self, arbol_parameters: Dict) -> Dict:
        """ save_arbol """
        try:
            if self.logger.isEnabledFor(logging.DEBUG):
                self.logger.debug("entering the 'save_arbol' method")            

            v_input_arbol = arbol_parameters["input_arbol"]

            v_saved_arbol = app.v_application.save_arbol(v_input_arbol)

            response = v_saved_arbol

        except Exception as ex:
            self.logger.info("save_arbol: %s", str(ex))
            abort(make_response(jsonify(message=str(ex)), 500))
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("finalizing the 'save_arbol' method")
        return response

    def get_arbol(self):
        """ get all data target types """
        try:
            if self.logger.isEnabledFor(logging.DEBUG):
                self.logger.debug("entering the 'get_arbol' method")
            
            v_get_arbol = app.v_application.get_arbol()

            response = v_get_arbol

        except Exception as ex:
            self.logger.info("remove_configcentro: %s", str(ex))
            abort(make_response(jsonify(message=str(ex)), 500))
        return response

    def get_ancestor(self, num_1, num_2):
        """ get all data target types """
        try:
            if self.logger.isEnabledFor(logging.DEBUG):
                self.logger.debug("entering the 'get_ancestor' method")

            get_ancestor = app.v_application.get_ancestor(num_1, num_2)

            response = get_ancestor

        except Exception as ex:
            self.logger.info("remove_configcentro: %s", str(ex))
            abort(make_response(jsonify(message=str(ex)), 500))
        return response        

CLASS_INSTANCE = ArbolResource()
