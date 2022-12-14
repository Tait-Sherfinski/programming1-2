import pygame

pygame.init()

# library of game contents
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
WIDTH = 400
HEIGHT = 500

player = pygame.image.load('Mario.webp')
fps = 60
font = pygame.font.Font('freesamsbold.ttf', 16)
timer = pygame.time.Clock()


screen = pygame.display.set_mode(WIDTH, HEIGHT)