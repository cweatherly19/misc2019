# dummy for code on arm
# don't need to necessarily print the messages, just helpful to know where we're at
# will receive the data as [x, y, z]
# the while loop is what the motor control code should be looping too
# so its continuously receiving a connection and fresh data
# pickles is for making legible, useable data
# right now can run with diagram.py to print the coordinates it's supes cool
# THIS SHOULD BE ON CONNOR'S CODE


import socket
import pickle

# next create a socket object
s = socket.socket()

port = 2187
s.bind(('', port))
print "socket binded to %s" %(port)
s.listen(5)
print "socket is listening"

c, addr = s.accept()
print 'Got connection from', addr
c.send('Thank you for connecting')


while True:
    xyz = c.recv(5000)

    input = pickle.loads(xyz)
    x = int(input[0])
    y = int(input[1])
    z = int(input[2])
    print x
    print y
    print z
    print input

# Close the connection with the client
c.close()
