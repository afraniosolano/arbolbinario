""" import packages """
import io
from typing import Dict
import config.config as config
import logging
import exception.exception as exception
import arbol.nodo as nodo
import arbol.arbol as arbol


class Application(object):
    """ Application class """

    def __init__(self, p_config: config.Config, p_arbol: arbol.Arbol) -> None:
        self.logger = logging.getLogger(__name__)
        self.arbol = p_arbol

    def save_arbol(self, p_input_arbol: str) -> Dict:
        """ save_arbol """
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("entering the 'save_arbol' method")

        v_datos = p_input_arbol.split(",")

        for dato in v_datos:
             v_temp = self.arbol.insertar(self.arbol.raiz, int(dato))
             if v_temp:
                self.arbol.raiz = v_temp
       
        v_result = self.arbol.to_dict()
                
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("finalizing the 'save_arbol' method")
        return v_result

    def get_arbol(self) -> Dict:
        """ get_arbol """
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("entering the 'get_arbol' method")

        v_result = self.arbol.to_dict()
                
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("finalizing the 'get_arbol' method")
        return v_result

    def get_ancestor(self, num_1, num_2):
        """ get_ancestor """
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("entering the 'get_ancestor' method")

        v_result = self.arbol.get_ancestor(num_2, num_1)
                
        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug("finalizing the 'get_ancestor' method")
        return v_result
