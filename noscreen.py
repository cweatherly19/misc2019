# ugh testing pygame

import pygame
from pygame.locals import *
pygame.init()

done = False
clock = pygame.time.Clock()

try:
    screen = pygame.display.set_mode((400,300))
    screen.fill(255,255,255)
except:
    while not done:
        clock.tick(10)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            else: # did something other than close
                print("congrats")
