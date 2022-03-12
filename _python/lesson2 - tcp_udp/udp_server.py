import socket

class Server:

    def __init__(self, udp_port, udp_ip):

        self.udp_port = udp_port
        self.udp_ip = udp_ip
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def getUdp_ip(self):
        return self.udp_ip

    def getUdp_port(self):
        return self.udp_port

    def createSocket(self):

        udp_ip = self.getUdp_ip()
        udp_port = self.getUdp_port()

        udp_socket = self.udp_socket

        print("[INFO] Socket criado!")
        udp_socket.bind((udp_ip, udp_port))

        while 1:
            d = udp_socket.recvfrom(1024)
            data = d[0]
            addr = d[1]
            
            if not data: 
                break
            
            data = data.decode('utf-8')
            reply = 'Ok...' + data
            reply = reply.encode('utf-8')
            
            udp_socket.sendto(reply , addr)
            print('Mensagem: ' + data.strip())
            
        udp_socket.close()


udp_ip = '127.0.0.1'

server = Server(8000, udp_ip)

server.createSocket()
