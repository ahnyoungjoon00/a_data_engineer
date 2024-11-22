class Response :
    def __init__(self, statusline:bytes, header = {}, body:bytes=b''):
        self.__statusline = statusline
        self.__header = header
        self.__body = body

    @property
    def statusline(self):
        return self.__statusline
    
    @property
    def header(self):
        return self.__header

    @property
    def body(self):
        return self.__body
