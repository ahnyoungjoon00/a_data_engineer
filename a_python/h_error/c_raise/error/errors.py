class IllegalPropertyError(Exception):
    def __init__(self, msg='부적절한 값입니다.'):
        self.msg = msg
    
    def __str__(self):
        return self.msg

class TimeoutError(Exception):
    def __str__(self):
        return '통신지연이 발생했습니다.'
        
