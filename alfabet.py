import pygame
import time

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

letters = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','R','S','Ś','T','U','W','V','X','Y','Z','Ź','Ż']

# assigning values to X and Y variable
X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Komunikacja Człowiek-Komputer')
font = pygame.font.Font('freesansbold.ttf', 32)

i=0

while True:
    display_surface.fill(white)

    text = font.render(letters[i], True, green, blue)
    time.sleep(2)
    i += 1s
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
