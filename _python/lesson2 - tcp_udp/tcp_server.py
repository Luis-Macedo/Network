import socket

class Server:

    def __init__(self, tcp_port, tcp_ip, buf_size):

        self.tcp_port = tcp_port
        self.tcp_ip = tcp_ip
        self.buf_size = buf_size
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def getTcp_ip(self):
        return self.tcp_ip

    def getTcp_port(self):
        return self.tcp_port
    
    def getBuf_size(self):
        return self.buf_size

    def createSocket(self):

        tcp_ip = self.getTcp_ip()
        tcp_port = self.getTcp_port()
        
        print("[INFO] Socket criado!")

        self.tcp_socket.bind((tcp_ip,tcp_port))
        print("[INFO] Socket está ligado à porta:",tcp_port)

        self.tcp_socket.listen(1)
        print("[INFO] Socket está escutando")

    def recieve(self):

        tcp_socket = self.tcp_socket
        client, address = tcp_socket.accept()
        buf_size = self.getBuf_size()

        print("[INFO] Endereço de conexão vindo de: ",address)

        print("[INFO] Recebendo dados do cliente...")
        data = client.recv(buf_size)

        print("[INFO] Decodificando dados do cliente...")
        data = data.decode('utf-8')

        print("[INFO] Ddaos recebidos do cliente:",data)

        msg = "Até mais!"
        msg = msg.encode('utf-8')

        print("[INFO] Enviando dados para o cliente...")
        client.send(msg)
        print("[INFO] Dados enviados com sucesso")

        print("[INFO] Desconectando o client...")
        client.close()

        print("[INFO] Desconectando socket...")
        tcp_socket.close()
        print("[INFO] Socket desconectado!")


tcp_ip = '127.0.0.1'
buf_size = 30

server = Server(8000, tcp_ip, buf_size)
server.createSocket()
server.recieve()