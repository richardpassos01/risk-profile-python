from http import HTTPStatus


class CustomError(Exception):
    def __init__(self, message, code=None, status=HTTPStatus.INTERNAL_SERVER_ERROR):
        super().__init__(message)
        self.message = str(message)
        self.code = code
        self.status = status