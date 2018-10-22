#following the tutorial on https://pythonspot.com/python-network-sockets-programming-tutorial/
import socket

HOST="127.0.0.1"		#standard loopack interface address(localhost)
PORT=65432				#port to listen on

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()

print("Connected by",addr)
while True:
	data=conn.recv(1024)
	if not data:
		break
	conn.sendall(data)