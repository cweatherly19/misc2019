import socket 		#Needed for networking
import os
import time
import sys
import pickle		#Used to transmit data to server
import linecache	#Used for diagnostics
import inspect		#Used for diagnostics

# Create a socket object
s = socket.socket()


oof = [1, 5, 9]

# Define the port on which you want to connect
port = 2197

# connect to the server on local computer
# first number if on computer: 127.0.0.1
# if on pi: 192.168.21.xxx, xxx being the chip #
s.connect(('127.0.0.1', port))





data = pickle.dumps(oof)	#Pickles the data [see ControlPyEvolvedCore for more information]
s.sendall(data)



# receive data from the server
print s.recv(200)
# close the connection
s.close()
