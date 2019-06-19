import sys
import time
import socket	#Needed for networking
import pickle	#Needed for transmission and reception of more complex data with our method of networking


loopMain = True	#Main loop boolean
loopConnection = False	#Loop boolean for the connection code
#-------------------------------------------------------------------------------
#===============================================================================

#FUNCTIONS======================================================================

#Function to clear the console (not actually used in this version, but here as a utility anyway)
def consoleClear():
	os.system('cls' if os.name == 'nt' else 'clear')	#Detects what OS is being cleared



#===============================================================================

def motorMove(ml0, ml1, ml2, ml3, ml4, ml5):
#Each of these items is a motor; each motor is an array of three values:
#MOTOR ID - which pins the motor occupies on the Pi
#MOVE PERCENTAGE - the math below converts a 0-100 scale to numbers the roboPi motors use (1000-2000)
#DIRECTIONAL MULTIPLIER - a factor that inverts the motor

	#Conversion math
    m0Move = int(1500 + ((float(ml0[2]) * (float(ml0[1] / 100) * 500))))
    m1Move = int(1500 + ((float(ml1[2]) * (float(ml1[1] / 100) * 500))))
    m2Move = int(1500 + ((float(ml2[2]) * (float(ml2[1] / 100) * 500))))
    m3Move = int(1500 + ((float(ml3[2]) * (float(ml3[1] / 100) * 500))))
    m4Move = int(1500 + ((float(ml4[2]) * (float(ml4[1] / 100) * 500))))
    m5Move = int(1500 + ((float(ml5[2]) * (float(ml5[1] / 100) * 500))))
    print m0Move
    print m1Move
    print m2Move
    print m3Move
    print m4Move
    print m5Move



#MAIN CODE======================================================================
#MAIN LOOP----------------------------------------------------------------------
while loopMain:
	addressIP = input("Enter IP address: ")
	addressPort = input("Enter your port #: ")

	#Makes sure the port is a valid int
	try:
		int(addressPort)
		loopConnection = True
	except:
		loopConnection = False

	#CONNECTION LOOP------------------------------------------------------------
	while(loopConnection):
#		try:	#On connection failure, will trigger exception
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as netS:	#Creates socket variable as netS
			print("Server initializing...")
			netS.bind((addressIP, int(addressPort)))	#Binds port to IP. On a RoboPi, it is the IP in the SSH command. On the Macs, check system preferences. Connectivity is all about IP Address (can be thought of an address for a skyscraper)...
			print("Server IP and Port Bound!") 			#... and ports (think of them as like room/appartment numbers in said skyscraper). Port can be a random number within a specific range (~1024-65535) as long as it is not already in use. Must either be on the same network, or be portforwarding said port.
			netS.listen(1)				#Opens up the specified IP's specified port for (x) number of connections, in this case, only 1
			conn, addr = netS.accept()	#Upon receiving a connection attempt, this accepts said attempt and labels it "conn".
			print("Server online!")
			with (conn):	#With the connection designated above...
				print ('Connected by', addr)
				iterations = 100	#Part of optional [default disabled] limiter of commands that can be received.
				while (iterations > 0):	#See above
					#iterations -= 1	#See above; enable to enable command count limiter.
					input = pickle.loads(conn.recv(262144))	#Receives transmission and uses the pickle library to decode it into lists. conn.recv(###) - ### is basically data size; see https://realpython.com/python-sockets/ for non-pickle version and a more thurough explanation.
					print("Input: " + str(input))
					motorMove(input[0], input[1], input[2], input[3], input[4], input[5])	#Takes unpickled data sent from client and plugs it into the motor move functions.

#		except Exception as e:	#Prints error on connection (or other) failures
#			print("CRITICAL ERROR")
#			print(e)
#			loopMain = False
#			break
	#---------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#===============================================================================
