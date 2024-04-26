import random
import pygame
from globals import CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT


class Food:
    def __init__(self, free_cells):
        self.spawn_food(free_cells)

    def spawn_food(self, free_cells):
        random_cell = random.choice(list(free_cells))
        self.x = random_cell[0]
        self.y = random_cell[1]

        self.rect = pygame.Rect(
            self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1
        )

    def update(self, screen):
        pygame.draw.rect(screen, "orange", self.rect)
