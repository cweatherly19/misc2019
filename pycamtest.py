# found this code, now trying to make it work better!


import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

#create fullscreen display 640x480
screen = pygame.display.set_mode((256,96),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(64,48))
webcam_two = pygame.camera.Camera(cam_list[1], (64,48))
webcam.start()
webcam_two.start()

while True:
    #grab image, scale and blit to screen
    imagen = webcam.get_image()
    imagen = pygame.transform.scale(imagen,(128,96))
    imaget = webcam_two.get_image()
    imaget = pygame.transform.scale(imaget,(128,96))
    
    screen.blit(imagen,(0,0))
    screen.blit(imaget,(129,0))
    
    #draw all updates to display
    pygame.display.update()

    # check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            webcam.stop()
            webcam_two.stop()
            pygame.quit()
            sys.exit()
