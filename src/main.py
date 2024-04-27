import pygame, sys, time
from Snake import Snake
from Food import Food
from globals import CELL_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT


BLACK = (0, 0, 0)
WHITE = (225, 225, 225)


def main():
    pygame.init()

    font_small = pygame.font.Font(None, 60)
    font_smaller = pygame.font.Font(None, 30)
    font_big = pygame.font.Font(None, 110)

    restart_button = pygame.Rect(
        (WINDOW_WIDTH - BUTTON_WIDTH) // 2,
        ((WINDOW_HEIGHT - BUTTON_HEIGHT) // 2) + 70,
        BUTTON_WIDTH,
        BUTTON_HEIGHT,
    )
    restart_text = font_smaller.render("Restart", True, BLACK)
    restart_text_rect = restart_text.get_rect(center=restart_button.center)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")

    free_cells = {
        (x, y)
        for x in range(WINDOW_WIDTH // CELL_SIZE)
        for y in range(WINDOW_HEIGHT // CELL_SIZE)
    }

    score = font_small.render("1", True, "white")
    score_rect = score.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT / 20) + 30))

    snake = Snake()
    free_cells -= set(snake.body)
    food = Food(free_cells)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if not (len(snake.body) > 1 and snake.direction == "up"):
                        snake.direction = "down"
                elif event.key == pygame.K_UP:
                    if not (len(snake.body) > 1 and snake.direction == "down"):
                        snake.direction = "up"
                elif event.key == pygame.K_RIGHT:
                    if not (len(snake.body) > 1 and snake.direction == "left"):
                        snake.direction = "right"
                elif event.key == pygame.K_LEFT:
                    if not (len(snake.body) > 1 and snake.direction == "right"):
                        snake.direction = "left"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    if restart_button.collidepoint(event.pos):
                        free_cells = {
                            (x, y)
                            for x in range(WINDOW_WIDTH // CELL_SIZE)
                            for y in range(WINDOW_HEIGHT // CELL_SIZE)
                        }
                        snake = Snake()
                        food = Food(free_cells)

        # BACKGROUND
        screen.fill(BLACK)

        # scrore
        score = font_small.render(f"{len(snake.body)}", True, "white")

        # update obstacles
        food.update(screen)
        snake.update(screen)

        # update free cells

        if snake.body[-1] == (food.x, food.y):
            snake.body.append((food.x, food.y))
            food.spawn_food(free_cells)

        screen.blit(score, score_rect)

        if not snake.alive:
            dead_text = font_big.render("You are dead", True, "white")
            text_rect = dead_text.get_rect(
                center=(WINDOW_WIDTH // 2, (WINDOW_HEIGHT // 2) - 20)
            )
            screen.blit(dead_text, text_rect)
            pygame.draw.rect(screen, WHITE, restart_button)
            screen.blit(restart_text, restart_text_rect)

        pygame.display.update()
        time.sleep(200 / 1000)


if __name__ == "__main__":
    main()
