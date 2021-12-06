import pygame
import time

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

letters = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','R','S','Ś','T','U','W','V','X','Y','Z','Ź','Ż']
X = 400
Y = 400
def display_text(text):
    text = font.render(text, True, green, blue)
    pygame.time.delay(1000)
    display_surface.blit(text, (X // 2, Y // 2))
    pygame.display.update()
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Komunikacja Człowiek-Komputer')
font = pygame.font.Font('freesansbold.ttf', 32)

display_surface.fill(white)

i=0

display_text('3..')
display_text('2..')
display_text('1..')
display_text('START')
while True:
    display_surface.fill(white)

    text = font.render(letters[i%len(letters)], True, green, blue)
    pygame.time.delay(1000)
    i += 1
    display_surface.blit(text, (X // 2, Y // 2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
