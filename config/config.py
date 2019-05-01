""" import packages """
from abc import ABC, abstractmethod


class Config(ABC):
    """ class Config """

    @abstractmethod
    def get_string(self, *args):
        """ get_string """
        raise NotImplementedError

    @abstractmethod
    def get(self, *args):
        """ get """
        raise NotImplementedError
