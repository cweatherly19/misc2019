import socket
import pickle
import RoboPiLib as RPL
import setup

s = socket.socket()
port = 7777
s.bind(('', port))
s.listen(5)
c, addr = s.accept()

print 'Got connection from', addr

# send a thank you message to the client.
c.send('Thank you for connecting')
m = c.recv(70)

input = pickle.loads(m)

M_R = int(input[0])
M_L = int(input[1])

RPL.pwmWrite(0,0,3)
RPL.pwmWrite(1,0,3)

print M_R
print M_L


# Close the connection with the client
c.close()
