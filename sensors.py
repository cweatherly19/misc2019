import RoboPiLib as RPL
import setup
import post_to_web as PTW
import time

start = time.time()
now = time.time()

pin = 6
content = 0
i = 0
average = [ ]
base = RPL.analogRead(pin)

while len(average) < 50:
    content = RPL.analogRead(pin)
    average.append(content)

base = sum(average) / len(average)


PTW.state['Start Time:'] = time.asctime(time.localtime())
# begins by averaging the first 1000 readings in order to get a base reading

while now - start < 1500:
    content = RPL.analogRead(pin)
    if base - content >= 3:
        PTW.state['CO2detect: '] = "Life possible - %i" % content
    elif base - content >= 15:
        PTW.state['CO2detect: '] = "Life certain - %i" % content
    else:
        PTW.state['CO2detect: '] = "No life detected - %i" % content

    now = time.time()
    minutes, seconds = divmod((now - start), 60)
    if minutes >=3:
        PTW.state['Driving time: '] = minutes - 3
    PTW.state['Minutes: '] = minutes
    PTW.state['Seconds: '] = round(seconds, 1)


    PTW.post()

PTW.state['Mission Complete.']
