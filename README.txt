Name: 				Xiaofu Niu
GT ID:				903438953
E-Mail:				xiaofu.niu@gatech.edu
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
Examples can be found in sample.txt

Protocal Description:
A client initiates a request by establishing a TCP connection to a particular port specified by user on a server. Each time client will send two operands and one operator to server. After finishing the calculation, server will send back the result to client. Client will decide which operands and operator to send based on RPN calculation rule. Server only process one operation at one time.
Session State:
	The server has only three states: idle, calculation and close. In idle state, server listen for requests from clients. On receiving a function message, it switches into calculation format, read input function, calculate and send result back to client. Then it resturns back to idle mode. After client finishes all calculation and close the socket, it sends a NULL string to server, and server will close its session and switch to close mode. Clients are responsible for handling multiple requests and decide which operation to do next, and server knows nothing about it.
Message Format
	The client and server communicate by sending ASCII messages. The server sends RPN function to server, and the server sends result of the function.
	- Function message
	The function message consists of the two operands and one operator, in the sequence of <operand 1> <operand 2> <operator>. Operands can be any integers, the range of integers depends on machine (-2^32 - 2^32-1 for 32-bit machine and -2^64-2^64-1 for 64-bit machine). Operators must be one of +,-,*,/. If the operator is /, the second operand can not be 0. All functions sent by client are valid. 
	- Result message
	The result messages contains only calculation result of the function it receives. The datatype is an integer in the range same as operands in function message.
	- End message
	When client finishes all calculation and close the socket, it sends an empty string to server. Server will close its socket and exit the program once it receives the end message.
