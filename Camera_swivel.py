from bsmLib import RPL
RPL.init()
import curses, time

screen = curses.initscr()
curses.noecho()
curses.halfdelay(1)

motor_pin = 1
key = ''
key_down = time.time()

while key != ord('q'):
    key = screen.getch()
    screen.clear()
    if key == ord('a'):
        RPL.servoWrite(motor_pin, 1000)
        key_down = time.time()
        screen.addstr('clockwise')
    if key == ord('d'):
        RPL.servoWrite(motor_pin, 2000)
        key_down = time.time()
        screen.addstr('counterclockwise')
    if time.time() - key_down > 0.5:
        RPL.servoWrite(motor_pin, 0)
        screen.addstr('stopped')
    if key == ord('q'):
        RPL.servoWrite(motor_pin, 0)
        curses.endwin()
