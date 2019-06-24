d_one = 62.0 #distance from shoulder to elbow
d_two = 48.0 #distance from elbow to wrist

x = d_two #starting x value
y = d_one #starting y value
z = 0.0 #starting z value
speed = 1 #starting speed (whole number between 1 and 4)

microsoft = apple = False #determine which opperating system is being used

print "Press '1' to end code"

def test(): #function for angle domains
    reach_length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    if reach_length > d_one + d_two or reach_length < d_one - d_two:
        return False


try: #if running on apple
    import sys, tty, termios #imports for no return command

    fd = sys.stdin.fileno() #unix file descriptor to define the file type
    old_settings = termios.tcgetattr(fd) #records the existing console settings

    tty.setcbreak(sys.stdin) #sets the style of input

    apple = True #computer type

except: #if running on microsoft
    import msvcrt #microsoft file for key input

    microsoft = True #computer type


quit = False #for breaking the motor loop with the '1' key command

import math #to calculate all angle values and error
try: #if not connected to a RoboPi, it can still run
    import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
    RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

    elbow_motor_speed = 200
    shoulder_motor_speed = 500

    distance_of_error = 3 #max distance arm can be away from intended point

    max_error = distance_of_error / math.sqrt(3) #to convert the error to the intiger unit of measurement

    shoulder_range = 840 #range of read value for the shoulder POT
    elbow_range = 775 #range of read value for the elbow POT
    swivel_range = 800 #(NUMBER HERE: NEED TO FIND POT AND ITS RANGE FOR THIS) #range of read value for the swivel POT

    shoulder_pul = 1 #shoulder pulse pin
    shoulder_dir = 2 #shoulder direction pin
    elbow_pul = 5 #elbow pulse pin
    elbow_dir = 6 #elbow direction pin
    swivel_continuous = 1 #pin for swivel motor
    ppin_shoulder = 5 #pin number for shoulder potentiometer
    ppin_elbow = 6 #pin number for elbow potentiomenter
    ppin_swivel = 7 #pin number for swivel potentiomenter

    print "shoulder_pul", shoulder_pul
    print "shoulder_dir", shoulder_dir
    print "elbow_pul", elbow_pul
    print "elbow_dir", elbow_dir
    print "swivel_continuous", swivel_continuous
    print "ppin_shoulder", ppin_shoulder
    print "ppin_elbow", ppin_elbow
    print "ppin_swivel", ppin_swivel

    RPL.pinMode(shoulder_pul, RPL.PWM) #set shoulder_pul pin as a pulse-width modulation output
    RPL.pinMode(shoulder_dir, RPL.OUTPUT) #set shoulder_dir pin to an output and write 1 to it
    RPL.pinMode(elbow_pul, RPL.PWM) #set elbow_pul pin as a pulse-width modulation output
    RPL.pinMode(elbow_dir, RPL.OUTPUT) #set elbow_dir pin to an output and write 1 to it

except:
    print 'Motors unrunnable: unable to reach RoboPiLib_pwm'


import socket
import pickle

s = socket.socket()
print "Socket successfully created"
port = 2187
s.bind(('', port))
print "socket binded to %s" %(port)
s.listen(5)
print "socket is listening"

c, addr = s.accept()
print 'Got connection from', addr
c.send('Thank you for connecting')

def key_reader():
    xyz = c.recv(5000)
    input = pickle.loads(xyz)
    x = int(input[0])
    y = int(input[1])
    z = int(input[2])
    print input
    return x, y, z


def motor_runner(x, y, z): #sends signals to all the motors based on potentiometer readings
    sqd_one = d_one ** 2
    sqd_two = d_two ** 2
    d_three = math.sqrt((y**2) + (x**2))
    a_elbow = math.acos((sqd_one + sqd_two - ((y**2) + (x ** 2))) / (2 * d_one * d_two))
    a_two = math.asin((d_two * math.sin(a_elbow) / d_three)) # angle between shoulder and wrist
    a_four = math.atan2(y , x) # angle between 0 line and wrist
    a_shoulder = round((a_four + a_two),4)  # shoulder angle

    reach_length = math.sqrt(x ** 2 + y ** 2 + z ** 2) #the momentary length of the arm

#    a_elbow = round(abs(elbow_value - math.pi), 4) #the converted angle of the elbow
#    try:
    if z > 0:
        a_swivel = round(math.acos(z / x), 4)
    elif z < 0:
        a_swivel = round(((math.pi / 2) + math.asin(math.fabs(z)/x)), 4)
    elif z == 0:
        a_swivel = round(math.pi / 2, 4)
#        a_swivel = round(math.asin(z / math.sqrt(x ** 2 + z ** 2)) + math.pi / 2, 4) #the swivel angle
#    except:
#        a_swivel = math.pi / 2 #the swivel angle when its angle doesn't matter

    try:
        #move shoulder motor
        pot_shoulder = RPL.analogRead(ppin_shoulder) * 3 * math.pi / (2 * shoulder_range) - math.pi / 4
        error_s = abs(pot_shoulder - a_shoulder) #how many degrees off the intended value the arm is
        calculated_error_s = error_s * d_two
        if calculated_error_s > max_error:
            if pot_shoulder > a_shoulder:
                RPL.digitalWrite(shoulder_dir, 0) #turn clockwise
            else:
                RPL.digitalWrite(shoulder_dir, 1) #turn counterclockwise
            RPL.pwmWrite(shoulder_pul, shoulder_motor_speed, shoulder_motor_speed * 2)
        else:
            RPL.pwmWrite(shoulder_pul, 0, shoulder_motor_speed * 2) #stops running while in range

        #move elbow motor
        pot_elbow = RPL.analogRead(ppin_elbow) * 3 * math.pi / (2 * elbow_range) - math.pi / 4
        error_e = abs(pot_elbow - a_elbow) #how many degrees off the intended value the arm is
        calculated_error_e = error_e * d_two
        if calculated_error_e > max_error:
            if pot_elbow > a_elbow:
                RPL.digitalWrite(elbow_dir, 0) #turn clockwise
            else:
                RPL.digitalWrite(elbow_dir, 1) #turn counterclockwise
            RPL.pwmWrite(elbow_pul, elbow_motor_speed, elbow_motor_speed * 2)
        else:
            RPL.pwmWrite(elbow_pul, 0, elbow_motor_speed * 2) #stops running while in range

        #move swivel motor
        pot_swivel = RPL.analogRead(ppin_swivel) * 3 * math.pi / (2 * swivel_range) - math.pi / 4
        error_sw = abs(pot_swivel - a_swivel) #how many degrees off the intended value the arm is
        if error_sw > max_error:
            if pot_swivel > a_swivel:
                RPL.servoWrite(swivel_continuous, 2000) #turn clockwise
            else:
                RPL.servoWrite(swivel_continuous, 1000) #turn counterclockwise
        else:
            RPL.servoWrite(swivel_continuous, 0) #stops running while in range

        if quit == True: #stop the motors when the code ends
            RPL.servoWrite(swivel_continuous, 0) #stops running while in range
            RPL.pwmWrite(elbow_pul, 0, elbow_motor_speed * 2) #stops running while in range
            RPL.pwmWrite(shoulder_pul, 0, shoulder_motor_speed * 2) #stops running while in range

    except: #to show the values of the motor arm
        print('[elbow, shoulder, swivel]:', [round(a_elbow, 4), round(a_shoulder, 4), round(a_swivel, 4)], '[Speed]:', [speed], '[x, y, z]:', [round(x, 2), round(y, 2), round(z, 2)])

while True:
    x, y, z = key_reader()
    motor_runner(x, y, z)


c.close()
