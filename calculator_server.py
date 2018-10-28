#following the tutorial on https://pythonspot.com/python-network-sockets-programming-tutorial/
#calculator_server.py
#@author Glenda
#@version 10/28/1028
#server for RPN calculator

import socket
import sys

if(len(sys.argv)<=1):
	print 'Using default port name:rpncalc, port number:65432'
	HOST='rpncalc'
	PORT=65432
elif(len(sys.argv)==2):
	print 'Using default port number:65432'
	HOST=sys.argv[1]
	PORT=65432
else:
	HOST=sys.argv[1]
	PORT=int(sys.argv[2])				#port to listen on

#establish connection
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()

#keep receiving instructions from client
while True:
	recv_str=conn.recv(1024)
	#send acknowledgement
	if(recv_str==''):
		conn.close()
		break
	out='Server Recieved:"'+recv_str+'"'
	print out
	#do the calculation
	data=recv_str.split()
	op1=int(data[0])
	op2=int(data[1])

	if data[2]=='+':
		result=op1+op2
	elif data[2]=='-':
		result=op1-op2
	elif data[2]=='*':
		result=op1*op2
	elif data[2]=='/':
		result=op1/op2
	conn.send(str(result))