import socket
from QRGenerator import QRGenerator 
class Server :
    def __init__(self):
        self.__port = 9898
        self.__buffersize = 1024

    """
    server socket : 서버가 상시로 열어두는 소켓
    client socket : 클라이언트와 통신을 위해, 클라이언트와 1:1로 열어두는 소켓
                    클라이언트가 접근하는 순간에 같이 열려서 받아주고, 클라이언트가 떠나면 닫음
                ex) 웹서버는 이런 식의 관리가 가능하여 서버의 부담을 줄일 수 있으나,
                    게임서버 같은 경우에는 실시간으로 정보를 내보내야하고, 몬스터 등 유지해야하는 것이 있어서,
                    실제 동접자 100만이면 socket이 100만개 열려있어야해서 자주 터지는 것.
    """
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("localhost", self.__port))
        server_socket.listen(5) # 대기할 수 있는 클라이언트의 숫자
        
        while(True) :
            client_socket, address = server_socket.accept() # 이때 위에 입력해주는 정보를 기반으로 서버소켓이 열린 상태에서 client socket을 기다리는
            request = client_socket.recv(self.__buffersize) # 클라이언트 소켓에 정보를 받는 함수 recv
            req_txt = str(request, encoding = "utf-8")

            # GET /qr http/1.1
            statusline = req_txt.splitlines()[0]
            status_tokens = statusline.split(" ")
            http_method = status_tokens[0]
            req_url = status_tokens[1]
            
            if ('/qr' not in req_url):
                client_socket.close()
                continue
            # ex) '/qr'?query1=a&query2=b&query3=c
            url_tokens = req_url.split("?")
            path = url_tokens[0]
            if len(url_tokens) >= 2 :
                query_string = url_tokens[1]
                param_dict = {}
                # [query1=a, query2=b, query3=c]
                params = query_string.split("&")

                for e in params :
                    token = e.split("=")
                    param_dict[token[0]] = token[1]
                
                client_socket.send(b'HTTP/1.1 200 OK\n')
                client_socket.send(b'Content-Disposition: attachment; filename="qr.jpg"\n\n')

                qr = QRGenerator()
                # client_socket.send(qr.generate(param_dict[token[0]]))
                # client_socket.send(bytes(param_dict[token[0]], encoding = "utf-8"))
                
                client_socket.close()
                continue

            client_socket.send(b'HTTP/1.1 200 OK\n\n')
            client_socket.send(b'hello world!')
            client_socket.close()
