Class Name: 		CS 6250 - Computer Network
Date: 				Oct.28 2018
Assignment: 		Programming Assignment


Files:
-rpnclient.py
-rpnserver.py
-README.txt
-sample.txt


How to run:
1	Open a terminal and run rpnserver.py:
	->python rpnserver.py <server port number>
	server port number is optional. If you do not specify one, it will use default port number 65432
2	Open another termimal and run rpnclient.py
	->python rpnclient.py <server port number> "<function to calculate>"
	server port number should match the one assigned to server previously.
	In the function, operands and operators are seperated with blank.
3	Close server.
	->^c
Examples can be found in sample.txt


Protocal Description:

A client initiates a request by establishing a TCP connection to a particular port specified by user on a server. After establishing the connection, client sends function to the server, and server do the calculation and sends back results. Server only process one operation at one time. Server serves clients in FCFS style and only handles one client at a time, neglacting any connection request it receives when serving a client.

Session State:
	- Client
	A client process one RPN function at a time, and immediately exits program once it finishes calculation and display the result. When it closes its socket, it sends a EOF message to server. client is stateless.
	- Server
	Server has four states: waiting for client, waiting for function, calculation and close.
	Waiting for client - Server listens on a port and wait for connection request. It establishes connection with client whoever comes first.
	Waiting for function - In this state, server listen for requests from clients. On receiving a function message, it switches into calculation format. When server receives a EOF message, it closes the connection and switches to waiting for client mode.
	Calculation - server reads input function, calculates and sends result back to client. Then it resturns back to waiting for function mode. 
	Close - User can close server whenever they want by pressing ^c.

Message Format
	The client and server communicate by sending ASCII messages. The server sends RPN function to server, and the server sends result of the function.
	- Function message
	The function message consists of the two operands and one operator, in the sequence of <operand 1> <operand 2> <operator>. Operands can be any integers, the range depends on machine (-2^32 - 2^32-1 for 32-bit machine and -2^64-2^64-1 for 64-bit machine). Operators must be one of +,-,*,/. If the operator is /, the second operand can not be 0. All functions sent by client are valid. 
	- Result message
	The result messages contains only calculation result of the function it receives. The datatype is an integer in the range same as operands in function message.
	- End message
	When client finishes all calculation and close the socket, it sends an EOF message (an empty string) to server. Server will exit the connection and wait for the next client once it receives the end message.