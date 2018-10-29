#calculator_client.py
#@author Glenda
#@version 10/29/1028
#client for RPN calculator without input syntex check

import socket
import sys

HOST='127.0.0.1'				#server's hostname or IP address
PORT=int(sys.argv[1])			#server port
ACK="ACKNOWLEDGE"

#initialize client
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
if(len(sys.argv)<3):
	print 'No input function.'
	sys.exit()
input_str=sys.argv[2].split()

stk=[]
for cnt in range(len(input_str)):
	c=input_str[cnt]
	if(c.lstrip('-').isdigit()):
		stk.append(int(c))
	else:
		if(len(stk)<2 or (c!='+' and c!='-' and c!='*' and c!='/')):
			print 'Input syntex error at',c
			s.close()
			break
		num2=stk.pop()
		num1=stk.pop()
		if(c=='/' and num2==0):
			print 'Can not devide by 0.'
			s.close()
			break
		string=str(num1)+' '+str(num2)+' '+c
		s.send(string)
		#wait for server to calculate
		result=s.recv(1024)
		if(cnt==len(input_str)-1):
			out='Client Received Final:'+result
			if(len(stk)!=0):
				print 'Input syntex error: no enough operators.'
			print out
			s.close()#send a NULL string to server
		else:
			out='Client Received:'+result
			print out
			stk.append(int(result))