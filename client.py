import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

client.send('Hello, FROM CLIENT!'.encode())

reply = client.recv(4096).decode()
print(reply)

client.close()