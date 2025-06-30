import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))

server.listen(5)
print('Waiting for connection...')

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send('Hello, FROM SERVER!'.encode())
    client.close()