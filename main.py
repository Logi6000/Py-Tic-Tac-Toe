import pygame
import time
import os

DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 640

pygame.init()

game_window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Tic Tac Toe")

def game_loop():
    game_running = True
    while game_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            print(event)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
