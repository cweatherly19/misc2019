import socket
import pickle

# Create a socket object
s = socket.socket()

oof = [0, 0]

# Define the port on which you want to connect
port = 7777

# connect to the server on local computer
# first number if on computer: 127.0.0.1
# if on pi: 192.168.21.xxx, xxx being the chip #
s.connect(('192.168.1.3', port))

data = pickle.dumps(oof)	#Pickles the data [see ControlPyEvolvedCore for more information]
s.sendall(data)


# receive data from the server
print s.recv(200)
# close the connection
s.close()
