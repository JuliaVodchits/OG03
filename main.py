import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
COLOR = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/png-transparent-archery-computer-icons-objective-sport-target-archery-circle.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/")
target_width = 60
target_height = 60
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

running = True
while running:
    pass

pygame.quit()