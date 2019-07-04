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

pin = 6
content = 0
i = 0
average = [ ]
base = RPL.analogRead(pin)

while len(average) < 50:
    content = RPL.analogRead(pin)
    average.append(content)


base = sum(average) / len(average)
print base
# begins by averaging the first 1000 readings in order to get a base reading

while True:
    content = RPL.analogRead(pin)
    if base - content >= 3:
        PTW.state['CO2detect: '] = "Life possible - %i" % content
    elif base - content >= 15:
        PTW.state['CO2detect: '] = "Life certain - %i" % content
    else:
        PTW.state['CO2detect: '] = "No life detected - %i" % content



    PTW.post()
