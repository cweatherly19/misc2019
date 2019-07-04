# timer

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



start = time.time()
now = time.time()

PTW.state['Start Time:'] = time.asctime(time.localtime())


# ^ setup

# begins by averaging the first 1000 readings in order to get a base reading

while now - start < 1080:
    now = time.time()
    minutes, seconds = divmod((now - start), 60)
    if minutes >=3:
        PTW.state['In competition: '] = True
    PTW.state['Minutes: '] = minutes
    PTW.state['Seconds: '] = round(seconds, 1)

    PTW.post()
