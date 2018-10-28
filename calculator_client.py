#calculator_client.py
#@author Glenda
#@version 10/28/1028
#client for RPN calculator without input syntex check

import socket
import sys

HOST=sys.argv[1]				#server's hostname or IP address
PORT=int(sys.argv[2])			#server port
ACK="ACKNOWLEDGE"

#initialize client
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
input_str=sys.argv[3].split()

stk=[]
for cnt in range(len(input_str)):
	c=input_str[cnt]
	if(c.lstrip('-').isdigit()):
		stk.append(int(c))
	else:
		if(len(stk)<2 or (c!='+' and c!='-' and c!='*' and c!='/')):
			print 'Input Syntex Error at',c
			s.close()
			break
		num2=stk.pop()
		num1=stk.pop()
		string=str(num1)+' '+str(num2)+' '+c
		s.send(string)
		#wait for server to calculate
		result=s.recv(1024)
		if(cnt==len(input_str)-1):
			out='Client Received Final:'+result
			print out
			s.close()#send a NULL string to server
		else:
			out='Client Received:'+result
			print out
			stk.append(int(result))