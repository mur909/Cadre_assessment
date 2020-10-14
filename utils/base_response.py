class BaseResponse(object):
    def __init__(self):
        self.code = 100
        self.error = ''
        self.data = ''
        self.info = ''

    @property
    def dict(self):
        return self.__dict__
