# CO2 sensor

# comands:
# ssh student@192.168.23.207
# password: Engineering!1
# python co2reading.py

# go to GUI: nav > config ip adress > data should be ssh number


import RoboPiLib as RPL
import setup
import post_to_web as PTW
import time

pi = True
co = 6
average = [ ]
content = 0

base = RPL.analogRead(co)
now = RPL.analogRead(co)
# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading

while True:

    if base - content >= 3:
        PTW.state['CO2detect: Life possible'] = content
    elif base - content >= 15:
        PTW.state['CO2detect: Life certain'] = content
    else:
        PTW.state['CO2detect: No life detected'] = content



    PTW.post()
