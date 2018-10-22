import socket

HOST="127.0.0.1"	#server's hostname or IP address
PORT=65432			#server port

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
s.sendall(b'Hello World')
data=s.recv(1024)
s.close()

print('Received',repr(data))