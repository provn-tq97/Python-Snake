import pygame
from globals import CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT


class Snake:
    def __init__(self):
        self.direction = "right"
        self.body = [(2, 5)]
        self.alive = True

    def update(self, screen):
        for i in self.body:
            pygame.draw.rect(
                screen,
                "green",
                pygame.rect.Rect(
                    i[0] * CELL_SIZE,
                    i[1] * CELL_SIZE,
                    CELL_SIZE - 1,
                    CELL_SIZE - 1,
                ),
            )

        if not self.alive:
            return

        head = list(self.body[0])

        if self.direction == "down":
            head[1] += 1
        elif self.direction == "up":
            head[1] -= 1
        elif self.direction == "right":
            head[0] += 1
        elif self.direction == "left":
            head[0] -= 1

        head[0] %= WINDOW_WIDTH // CELL_SIZE
        head[1] %= WINDOW_HEIGHT // CELL_SIZE

        self.body.insert(0, tuple(head))
        self.body.pop()

        self.check_collision()

    def check_collision(self):

        if self.body[0] in self.body[1:]:
            self.dead()

        # head_x, head_y = self.body[0]
        # if (
        #     head_x < 0
        #     or head_x >= WINDOW_WIDTH // CELL_SIZE
        #     or head_y < 0
        #     or head_y >= WINDOW_HEIGHT // CELL_SIZE
        # ):
        #     self.dead()

    def dead(self):
        self.alive = False
