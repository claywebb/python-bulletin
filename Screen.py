import pygame
import glob
import sys
import os


__DIRPATH = "/home/pi/Images/" # Directory of Images (with trailing backslash)
__WIDTH, __HEIGHT = 1920, 1080 # Screen resolution for scaling purposes
__DELAY = 7000 # Time in Milliseconds (1000 ms = 1 second)

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
done = False
images = []

# os.system("rsync -avzr --delete pi@76.190.192.76:~/Images ~/")
os.system('rsync -avzr --delete -e "ssh -i $HOME/.ssh/bulletin" eboard@76.190.192.76:~/Images %s' %(__DIRPATH))


def getImages():
    imagePaths = []
    imagePaths = glob.glob(__DIRPATH+"*.png") + glob.glob(__DIRPATH+"*.PNG") + glob.glob(__DIRPATH+"*.jpg") + glob.glob(__DIRPATH+"*.JPG")

    imagePaths.sort()

    print(imagePaths[:])

    #del imagePaths[-1]

    images = []

    for file in imagePaths:
        if file != "":
            images.append(pygame.image.load(file))
    return images;

images = getImages()

while not done:

    for i in images:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                sys.exit()

        screen.fill((0,0,0))
        screen.blit(pygame.transform.scale(i, (__WIDTH, __HEIGHT)), (0,0))
        pygame.display.flip()
        pygame.time.delay(__DELAY)

    os.system("rsync -avzr --delete pi@76.190.192.76:~/Images ~/")

    images = getImages()

