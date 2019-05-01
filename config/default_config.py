""" import packages """
import json
import os
import logging
import logging.config
from typing import List
import yaml
import config.config as config_abs


class DefaultConfig(config_abs.Config):
    """ class DefaultConfig """

    def __init__(self) -> None:
        config_filename = 'config/config.json'
        if 'CONFIG_FILE' in os.environ:
            config_filename = os.environ["CONFIG_FILE"]

        with open(config_filename) as v_file:
            self.config = json.loads(v_file.read())

        logging_config_file = 'config/logging.yml'
        if 'LOGGING_CONFIG_FILE' in os.environ:
            logging_config_file = os.environ["LOGGING_CONFIG_FILE"]

        with open(logging_config_file) as v_file:
            v_d = yaml.load(v_file)
            v_d.setdefault('version', 1)
            logging.config.dictConfig(v_d)

    def get_string(self, *args: List) -> str:
        v_value = self.config
        for arg in args:
            #print("arg: "+ arg)
            if type(v_value) is dict and arg in v_value:
                v_value = v_value[arg]
            else:
                return ""
            #print(v_value)
        if type(v_value) is str:
            return v_value
        return ""

    def get(self, *args: List) -> str:
        v_value = self.config
        for arg in args:
            if type(v_value) is dict and arg in v_value:
                v_value = v_value[arg]
            else:
                return ""
        return v_value
