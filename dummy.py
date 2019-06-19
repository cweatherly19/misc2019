# dummy for code on arm
# first of all import the socket library
import socket
import pickle

# next create a socket object
s = socket.socket()
print "Socket successfully created"

port = 2187
s.bind(('', port))
print "socket binded to %s" %(port)
s.listen(5)
print "socket is listening"

c, addr = s.accept()
print 'Got connection from', addr

# send a thank you message to the client.
c.send('Thank you for connecting')
while True:
    xyz = c.recv(5000)

    input = pickle.loads(xyz)
    print input

# Close the connection with the client
c.close()
