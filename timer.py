# timer
# go to GUI: nav > config ip adress > data should be ssh number

import post_to_web as PTW
import time


start = time.time()
now = time.time()

PTW.state['Start Time:'] = time.asctime(time.localtime())

while now - start < 1500:
    now = time.time()
    minutes, seconds = divmod((now - start), 60)
    if minutes >=3:
        PTW.state['Driving time: '] = minutes - 3
    PTW.state['Minutes: '] = minutes
    PTW.state['Seconds: '] = round(seconds, 1)

    PTW.post()

PTW.state['Mission Complete.']
