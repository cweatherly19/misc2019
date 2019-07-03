# CO2 sensor

# comands:
# ssh student@192.168.23.207
# password: Engineering!1
# python co2reading.py

# go to GUI: nav > config ip adress > data should be ssh number


import RoboPiLib as RPL
import setup
import post_to_web as PTW
import time, math

pi = True
co = 6
average = [ ]
base = 0
content = 0


frontr = RPL.analogRead(fr)
frontl = RPL.analogRead(fl)
sidel = RPL.analogRead(sl)
sider = RPL.analogRead(sr)


fr = 2
fl = 1
sl = 0
sr = 3

start = time.time()
now = time.time()

PTW.state['Start Time:'] = time.asctime(time.localtime())

try:
    RPL.analogRead(co)
except:
    pi = False
    base = 458
# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading

while now - start < 1080:
    if pi == True:
        content = RPL.analogRead(co)

        frontr = RPL.analogRead(fr)
        frontl = RPL.analogRead(fl)
        sidel = RPL.analogRead(sl)
        sider = RPL.analogRead(sr)



    else:
        content = 357
    if base - content >= 30:
        PTW.state['CO2detect: Life possible']

    elif base - content >= 50:
        PTW.state['CO2detect: Life certain'] = 3

    else:
        PTW.state['CO2detect: No life detected'] = 1

    PTW.state['Co2 data: '] = content
    now = time.time()
    minutes, seconds = divmod((now - start), 60)
    PTW.state['Minutes: '] = minutes
    PTW.state['Seconds: '] = round(seconds, 1)

    PTW.post()
