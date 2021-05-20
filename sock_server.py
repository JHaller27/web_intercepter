import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('0.0.0.0', 8800))
    sock.listen(1)

    print('Listening...')
    while True:
        (clientsock, addr) = sock.accept()
        print(addr)
        clientsock.send(bytes())
