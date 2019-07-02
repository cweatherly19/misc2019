# using arrow keys! also multiple angles! sideview and topview
# notes: can use continuously, but use one key at a time in an orderly fashion

# able to change z coordinate, and see change on topview.
# z is a plane, w is a dummy plane
# elbow is working
# don't cross y axis

# now integrating grasper movement too

# 0 = True, 1 = False

d_one = 62 # the distance from shoulder to elbow
d_two = 48 # distance from elbow to wrist

#the files needed to run the code
import pygame, math, time, socket, pickle
from pygame.locals import *

pygame.init()

#define the colors for the display
white = (255,255,255); black = (0,0,0)
red = (255,0,0); green = (127, 232, 134)
blue = (102, 136, 214); pink = (232, 13, 119)
grey = (203, 206, 214)

#dimentions of Pygame screen
display_width = 800
display_height = 450
screen = pygame.display.set_mode((display_width,display_height))
screen.fill(white)

#set the size of the step each input takes
step = 2

#set the origin of the side view
originx = 175
originy = 250

#set the origin of the top view
toriginz = 550
toriginw = 250

#defining variables so no error occurs
x, y, z, w = d_two, d_one, 0, d_two
xo, yo = x, y
x_change = y_change = z_change = 0

#setting up socket connection
s = socket.socket()
port = 2187
xyz = [x, y, z]


gopen = gclose = wup = wdown = 1
#gopen = gclose = wup = wdown = True

#set up kill commands
done = False
connect = True

def ik(x, y, z): # here is where we do math
    d_three = math.sqrt(y ** 2 + x ** 2)# determining distance from shoulder to wrist
    if d_three < d_one + d_two and d_three > d_one - d_two and y > -24:

        a_shoulder = math.acos((d_three ** 2 + d_one ** 2 - d_two ** 2) / (2 * d_one * d_three)) + math.atan2(y, x) #angle of shoulder

        xe = d_one * math.cos(a_shoulder)
        ze = xe * z / x
        ye = d_one * math.sin(a_shoulder)

        return xe, ye, ze

    else:
        return False

    #update the screen
    pygame.display.flip()

def test(x, y, z): #function for domains
    reach_length = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    if reach_length > d_one + d_two or reach_length < d_one - d_two or y > -24:
        return False

def pos(x, y, z):
    x_change = y_change = z_change = 0
    gopen = gclose = wup = wdown = 1
    #gopen = gclose = wup = wdown = True

    if event.type == pygame.KEYDOWN:
        # what key are they pressing? move accordingly
        if event.key == pygame.K_ESCAPE:
            done = True
            return done
        elif event.key == pygame.K_a:
            x_change = -step
            if test(x, y, z) == False:
                x_change = 0
        elif event.key == pygame.K_d:
            x_change = step
            if test(x, y, z) == False:
                x_change = 0
        elif event.key == pygame.K_w:
            y_change = step
            if test(x, y, z) == False:
                y_change = 0
        elif event.key == pygame.K_s:
            y_change = -step
            if test(x, y, z) == False:
                y_change = 0
        elif event.key == pygame.K_q:
            z_change = -step
            if test(x, y, z) == False:
                z_change = 0
        elif event.key == pygame.K_e:
            z_change = step
            if test(x, y, z) == False:
                z_change = 0
        elif event.key == pygame.K_j:
            gopen = 0
            #gopen = False
        elif event.key == pygame.K_l:
            gclose = 0
            #gclose = False
        elif event.key == pygame.K_k:
            wup = 0
            #wup = False
        elif event.key == pygame.K_i:
            wdown = 0
            #wdown = False

    return x_change, y_change, z_change, gopen, gclose, wup, wdown

# s.connect(('127.0.0.1', port))
# tests if you can connect
try:
    s.connect(('192.168.21.135', port))
    print("connection successful")
except:
    print("No connection")
    connect = False

#check for inputs
clock = pygame.time.Clock()

#loop to run and update the screen
while not done:
    clock.tick(60)
    # determine where want to be
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        else: # did something other than close
            try:
                x_change, y_change, z_change, gopen, gclose, wup, wdown = pos(x,y,z) # figure out the change
            except:
                done = True

    # move the change amount
    x += x_change
    y += y_change
    z += z_change

    if x_change and z_change == 0:
        w = math.sqrt(x ** 2 - z ** 2)
    elif x_change != 0:
        w = math.sqrt(x ** 2 - z ** 2)
    elif z_change != 0:
        x = math.sqrt(w ** 2 + z ** 2)

    #set the screen circle's colorings depending on position
    if gopen == 0:
    #if gopen == False
        pygame.draw.circle(screen, red, (350, 20), 10, 0)
    elif gclose == 0:
    #elif gclose == False
        pygame.draw.circle(screen, green, (350, 20), 10, 0)
    else:
        pygame.draw.circle(screen, black, (350, 20), 10, 0)

    if wup == 0:
    #if wup == False:
        pygame.draw.circle(screen, red, (450, 20), 10, 0)
    elif wdown == 0:
    #elif wdown == Fale:
        pygame.draw.circle(screen, green, (450, 20), 10, 0)
    else:
        pygame.draw.circle(screen, white, (450, 20), 10, 0)

    if ik(x, y, z) != False:
        # determine elbow point
        xe, ye, ze = ik(x, y, z)
        if xe == 0:
            we = 0
        else:
            we = math.sqrt(xe ** 2 - ze ** 2)
            if xe < 0:
                we = -we

        #so Pygame can move and not reset the origins
        xo = x + originx; yo = originy - y; zo = toriginz + z
        xe = xe + originx; ye = originy - ye; ze = toriginz + ze

        # draw lines
        #pygame.draw.lines(screen, blue, False, [[originx,originy], [xe, ye], [xo, yo]], 5) # sideview
        pygame.draw.line(screen, blue, (xe, ye), [(xo), (yo)], 5)
        pygame.draw.line(screen, pink, (originx, originy), (xe, ye), 5)

        pygame.draw.line(screen, blue, (toriginz, toriginw), [(zo), (toriginw - w)], 5)
        pygame.draw.line(screen, pink, (toriginz, toriginw), (ze, toriginw - we), 5)
    else: # out of range so stay
        pygame.draw.lines(screen, black, False, [[originx,originy], [xe, ye], [xo, yo]], 5)
        pygame.draw.circle(screen, pink, (x + originx, originy - y), (5), 0)
    if connect == True:
        xyz = [x, y, z, gopen, gclose, wup, wdown]
        data = pickle.dumps(xyz, protocol = 2)
        #output = 'Thank you for connecting'
        s.sendall(data)

    #s.send(xyz)

    # Be IDLE friendly
    pygame.draw.rect(screen, red,(50, 50, 100, 50))

    pygame.display.update()
    screen.fill(grey)
    pygame.draw.circle(screen, white, (originx, originy), (d_one + d_two), 0)
    pygame.draw.circle(screen, grey, (originx, originy), (d_one - d_two), 0)
    # topview
    pygame.draw.circle(screen, white, (toriginz, toriginw), (d_one + d_two), 0)
    pygame.draw.circle(screen, grey, (toriginz, toriginw), (10), 0)
    pygame.draw.rect(screen, grey, [0, (originy + 24), display_width, display_width])

#closes the imported files
s.close()
pygame.quit()
