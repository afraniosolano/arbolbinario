""" exception module """
import json
import jsonpickle

def format_error_message(msg: str) -> str:
    """ format_error_message """
    res = {"message": str(msg)}
    v_res = jsonpickle.encode(res, unpicklable=False)
    json_response = json.loads(v_res)
    return json_response


class IllegalArgumentError(ValueError):
    pass

class UnauthorizedUser(Exception):
    """ UnauthorizedUserv class """

    def __init__(self, p_user_name: str) -> None:
        self.user_name = p_user_name
        self._class = self.__class__
        Exception.__init__(self)

    def __str__(self) -> str:
        json_object = jsonpickle.encode(self, unpicklable=False)
        return str(json.loads(json_object))


class UserNotFound(Exception):
    """ UserNotFound class """

    def __init__(self, p_user_name: str) -> None:
        self.account_id = p_user_name
        Exception.__init__(self)


class InvalidFormatException(Exception):
    """ InvalidFormatException class """

    def __init__(self, prop: str, message: str) -> None:
        self.prop = prop
        self.message = message
        Exception.__init__(self)


class InvalidCall(Exception):
    """ InvalidCall class """

    def __init__(self) -> None:
        Exception.__init__(self)

class NullParameter(Exception):
    """ NullParameter class """

    def __init__(self, p_message: str) -> None:
        super().__init__()
        self.message = p_message
        Exception.__init__(self)
        self.class_exception = self.__class__ 
        
    def __str__(self):
        json_object = jsonpickle.encode(self, unpicklable=False)
        return str(json.loads(json_object))


class InvalidType(Exception):
    """ NullParameter class """

    def __init__(self, p_type: str) -> None:
        self.type = p_type
        Exception.__init__(self)


class AccountNotFound(Exception):
    """ Exceptions AccountNotFound """

    def __init__(self, p_account_id: str) -> None:
        self.account_id = p_account_id
        Exception.__init__(self)

#----------------------------------------------------------------------------------------------------


