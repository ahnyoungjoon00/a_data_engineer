import socket
from QRGenerator import QRGenerator

class Server:
    def __init__(self):
        self.__port = 9898
        self.__buffersize = 1024

    """
    server socket : 서버가 상시로 열어두는 소켓
    client socket : 클라이언트와 통신을 위해, 클라이언트와 1:1로 열어두는 소켓
    """
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', self.__port))
        server_socket.listen(5) # 대기할 수 있는 클라이언트의 숫자

        while(True):
            client_socket, address = server_socket.accept()
            request = client_socket.recv(self.__buffersize)
            req_txt = str(request, encoding='utf-8')
            statusline = req_txt.splitlines()[0]
            status_tokens = statusline.split(' ')

            http_method = status_tokens[0]
            req_url = status_tokens[1]

            if('/qr' not in req_url):
                client_socket.close()
                continue

            # '/qr?query1=a&query2=b&query3=c
            url_tokens = req_url.split('?')
            path = url_tokens[0]

            if(len(url_tokens) >= 2):
                query_string = url_tokens[1]

                # query1=a, query2=b, query3=c
                param_dict = {}
                params = query_string.split('&')

                for e in params:
                    token = e.split('=')
                    param_dict[token[0]] = token[1]
                
                client_socket.send(b'HTTP/1.1 200 OK\n')
                client_socket.send(b'Content-Disposition: attachment; filename="qr.png"\n\n')
                qr = QRGenerator()
                client_socket.send(qr.generate(param_dict[token[0]]))
                client_socket.close()
                continue
            
            client_socket.send(b'HTTP/1.1 200 OK\n\n')
            client_socket.send(b'hello world')


                




