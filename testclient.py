import socket 		#Needed for networking
import os
import time
import sys
import pygame		#Used for movement functions
import pickle		#Used to transmit data to server
import linecache	#Used for diagnostics
import inspect		#Used for diagnostics

motorRight = [0, 0, 1]		#List of important values for motors
motorLeft = [1, 0, 1]
motorRight2 = [2, 0, 1]
motorLeft2 = [3, 0, 1]
motorSteer = [4, 0, 1]
motorEmpty = [5, 0, 1]
mS = [motorRight, motorLeft, motorRight2, motorLeft2, motorSteer, motorEmpty] #List of lists to call


HOST = input("Enter IP address: ") #Defines IP address
PORT = input("Enter your port #: ") #Defines port number

PORT = checkAndInputInt(PORT)
if PORT != -1:
	loopConnection = True

while loopConnection == True:
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as netS: #Defines a socket and names it "netS"
				print ("Testing connection...")
				PORT = int(PORT)
				netS.connect((HOST, PORT)) #Attempts to connect to the port of the given IP; see ControlPyEvolvedCore for more detailed information about ports/IP
				print ("Client connected!")
				loopMenuMain = True
				#MAIN MENU LOOP-----------------------------------------------------------------------------------
				while loopMenuMain == True:
                    #Sends data with every change in movement status
					data = pickle.dumps(mS)	#Pickles the data [see ControlPyEvolvedCore for more information]
					netS.sendall(data)	#Transmits the pickled data

		except Exception as e:
			print("CRITICAL ERROR")
			print (e)
			loopMain = False
			break
