#following the tutorial on https://pythonspot.com/python-network-sockets-programming-tutorial/
#calculator_server.py
#@author Glenda
#@version 10/29/1028
#server for RPN calculator

import socket
import sys

HOST='127.0.0.1'
BUFF_SIZE=1024
OVERFLOW='OVERFLOW'
if(len(sys.argv)<=1):
	print 'Using default port number:65432'
	PORT=65432
elif(len(sys.argv)==2):
	PORT=int(sys.argv[1])

#initialize socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))

while True:
	#wait for client connection
	s.listen(1)
	conn,addr=s.accept()
	print "=============================================="
	#keep receiving instructions from client
	while True:
		recv_str=conn.recv(BUFF_SIZE)
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
			if(op1*op2<0 and op1%op2!=0):#6/-132=0
				result=op1/op2+1
			else:
				result=op1/op2
		#OVERFLOW case
		if(sys.getsizeof(result)>BUFF_SIZE):
			conn.send(OVERFLOW)
		else:
			conn.send(str(result))