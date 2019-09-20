import pygame
import random

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BALL_SIZE = 8


def player(window, x, y1, y2):
    pygame.draw.rect(window, WHITE, [x, 0, 20, 10], 0)
    pygame.draw.rect(window, WHITE, [x, 390, 20, 10], 0)
    pygame.draw.polygon(window, WHITE, [[0, y1], [0, y2], [10, y2], [10, y1]], 0)


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0


def make_ball():
    one = Ball()
    one.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    one.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)

    one.change_x = random.randrange(-2, 3)
    one.change_y = random.randrange(-2, 3)

    return one


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong no Walls")

done = False
clock = pygame.time.Clock()
pygame.mouse.set_visible(0)

ball_list = []
ball = make_ball()
ball_list.append(ball)

x_coord = 15
y1_coord = 0
y2_coord = 20

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x_coord > 0:
                    x_coord = -1

            elif event.key == pygame.K_RIGHT:
                if x_coord < 380:
                    x_coord = +1

            elif event.key == pygame.K_UP:
                if y1_coord > 0:
                    y1_coord = -1
                    y2_coord = -1

            elif event.key == pygame.K_DOWN:
                if y2_coord < 400:
                    y1_coord = +1
                    y2_coord = +1

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_coord = x_coord + 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y1_coord = y1_coord + 0
                y2_coord = y2_coord + 0

    screen.fill(BLACK)

    player(screen, x_coord, y1_coord, y2_coord)

    pygame.draw.line(screen, WHITE, [200, 0], [200, 50], 5)
    pygame.draw.line(screen, WHITE, [200, 60], [200, 110], 5)
    pygame.draw.line(screen, WHITE, [200, 120], [200, 170], 5)
    pygame.draw.line(screen, WHITE, [200, 180], [200, 230], 5)
    pygame.draw.line(screen, WHITE, [200, 240], [200, 290], 5)
    pygame.draw.line(screen, WHITE, [200, 300], [200, 350], 5)
    pygame.draw.line(screen, WHITE, [200, 360], [200, 400], 5)

    computerLeft = pygame.draw.polygon(screen, WHITE, [[400, 400], [400, 380], [390, 380], [390, 400]], 0)
    computerTop = pygame.draw.rect(screen, WHITE, [365, 0, 20, 10], 0)
    computerBottom = pygame.draw.rect(screen, WHITE, [365, 390, 20, 10], 0)

    for ball in ball_list:
        ball.x += ball.change_x
        ball.y += ball.change_y

        if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
            ball.change_y *= -1
        if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
            ball.change_x *= -1

    for ball in ball_list:
        pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
