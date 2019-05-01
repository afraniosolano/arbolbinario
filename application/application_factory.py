""" Module ApplicationFactory """
import config.config as config
import application.application as application
import arbol.arbol as arbol

class ApplicationFactory():
    """ class Repository """

    @staticmethod
    def factory(p_config: config.Config) -> application.Application:
        """ factory """
        v_arbol = arbol.Arbol()
        return application.Application(p_config, v_arbol)
