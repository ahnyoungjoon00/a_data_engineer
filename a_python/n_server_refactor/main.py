from infra.Server import Server
from infra import Dispatcher
from domain.QRview import QRview

if __name__ == "__main__" :
    path_dict = {"/qr": QRview()}

    Server().start_server(Dispatcher(path_dict))