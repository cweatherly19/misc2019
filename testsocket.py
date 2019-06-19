# first of all import the socket library
import socket

c = 0
x = 0
y = 0
z = 0


# next create a socket object
s = socket.socket()
print "Socket successfully created"

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 2197

# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', port))
print "socket binded to %s" %(port)

# put the socket into listening mode
s.listen(5)
print "socket is listening"

# a forever loop until we interrupt it or
# an error occurs


   # Establish connection with client.
c, addr = s.accept()
print 'Got connection from', addr

# send a thank you message to the client.
c.send('Thank you for connecting')
m = c.recv(70)

# Close the connection with the client
c.close()


m = " %s " % m
print m

m.split(' ')
for i in s.split(' '):
    c += 1
    if c == 1:
        x = int(i)
    if c == 2:
        y = int(i)
    if c == 3:
        z = int(i)

print "x: %d " % x
print "y: %d " % y
print "z: %d " % z
