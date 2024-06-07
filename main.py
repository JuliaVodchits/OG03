import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def get_target_x():
    return random.randint(0, SCREEN_WIDTH - target_width)


def get_target_y():
    return random.randint(0, SCREEN_HEIGHT - target_height)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/icon1.png")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 60
target_height = 60
target_x = get_target_x()
target_y = get_target_y()
score = 0


color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                score += 1
                target_x = get_target_x()
                target_y = get_target_y()
    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

print("Результат:", score)
pygame.quit()
