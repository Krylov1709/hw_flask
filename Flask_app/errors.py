

class HttpException(Exception):

    def __init__(self, statu_code: int, message: str | dict | list):
        self.status_code = statu_code
        self.message = message
