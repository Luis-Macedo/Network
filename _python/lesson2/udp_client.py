import socket

class Client:

    def __init__(self, udp_port, udp_ip):
        
        self.udp_port = udp_port
        self.udp_ip = udp_ip
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def getUdp_ip(self):
        return self.udp_ip

    def getUdp_port(self):
        return self.udp_port

    def sendMessage(self):

        udp_socket = self.udp_socket
        udp_port = self.getUdp_port()
        udp_ip = self.getUdp_ip()

        msg = "teste com udp"
        msg = msg.encode('utf-8')

        udp_socket.sendto(msg, (udp_ip, udp_port))
        
        data = udp_socket.recvfrom(1024)

        reply = data[0]
        reply = reply.decode('utf-8')
        
        print('Resposta do servidor : ' + reply)

        udp_socket.close()
            

udp_ip = '127.0.0.1'
client = Client(8000, udp_ip)
client.sendMessage()
