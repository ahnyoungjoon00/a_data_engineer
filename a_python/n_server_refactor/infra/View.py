from abc import *
from infra.Request import Request

class View(ABC) :
    
    @abstractmethod
    def do_get(req:Request) :
        pass