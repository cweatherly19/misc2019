# ugh testing pygame

import sys
import pygame
from pygame.locals import *
import pygame.camera
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()
pygame.camera.init()

done = False

cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(32,24))
webcam.start()


#grab image, scale and blit to screen
imagen = webcam.get_image()
print("yike")

webcam.stop()
pygame.quit()
sys.exit()
