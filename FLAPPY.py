import random
import sys

import pygame

FPS = 60
'''
IMAGE SECTION
'''
BACKGROUND_IMAGE = "images/background.png"
GROUND_IMAGE = "images/ground.png"
PIPE = "images/pipe.png"
BIRD = "images/bird.gif"
BIRD_U = "images/bird_wing_up.png"
BIRD_D = "images/bird_wing_down.png"
'''
HEIGHT AND WIDTH
'''
HEIGHT = 700
WIDTH = 1200
PIPE_WIDTH = 100
PIPE_HEIGHT = 500
HORIZONTAL_GAP = 500
MOV = 7
'''
PYGAME INNIT
'''
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FLAPPY")
clock = pygame.time.Clock()
'''
LOAD IMAGES::::::::::::::::::::::::::::::::::::::::
BACKGROUND
'''
bg = pygame.image.load(BACKGROUND_IMAGE)
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
'''
GROUND
'''
ground = pygame.image.load(GROUND_IMAGE).convert()
ground_height = ground.get_height()
'''
PIPE
'''
pipe_image = pygame.image.load(PIPE)
pipe = pygame.transform.scale(pipe_image, (PIPE_WIDTH, PIPE_HEIGHT))
pipe_height = pipe.get_height()
CURRENT_POSITION = 1
POSITION_PIPE1 = WIDTH
POSITION_PIPE2 = WIDTH + HORIZONTAL_GAP

flipped_pipe = pygame.transform.flip(pipe, False, True)
'''
PIPE LOGIC
'''
PIPE_TYPE_LIST = [50, 100, 200, 150, 250, 300, 350, 75, 225, 325]
X = random.choice(PIPE_TYPE_LIST)
Y = random.choice(PIPE_TYPE_LIST)
'''
BIRD
'''
# Bird properties
bird = pygame.image.load(BIRD).convert_alpha()
bird = pygame.transform.scale(bird, (50, 50))
bird_u = pygame.image.load(BIRD_U).convert_alpha()
bird_u = pygame.transform.scale(bird_u, (50, 50))
bird_d = pygame.image.load(BIRD_D).convert_alpha()
bird_d = pygame.transform.scale(bird_d, (50, 50))

bird_x = 200
bird_y = HEIGHT // 2
bird_vel = 0
GRAVITY = 0.5
FLAP_STRENGTH = -5
time_ = 0

'''
SCORE
'''
SCORE = 0
font = pygame.font.SysFont("Arial", 50, bold=True)
running = True


def GAME_OVER(SCORE):
    font1 = pygame.font.SysFont("Arial", 113, bold=True)

    waiting = True
    while waiting:
        game_over = font1.render(f" GAME OVER : SCORE = {int(SCORE)}", True, (0, 0, 0))

        bg1 = pygame.image.load(BACKGROUND_IMAGE)
        bg1 = pygame.transform.scale(bg1, (WIDTH, HEIGHT))
        screen.blit(bg1, (0, 0))
        screen.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, HEIGHT // 2 - game_over.get_height() // 2))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    screen.blit(ground, (0, HEIGHT - ground_height + 100))

    POSITION_PIPE1 = POSITION_PIPE1 - MOV
    CURRENT_PIPE_HEIGHT1 = HEIGHT - pipe_height + X
    screen.blit(pipe, (POSITION_PIPE1, CURRENT_PIPE_HEIGHT1))
    screen.blit(flipped_pipe, (POSITION_PIPE1, CURRENT_PIPE_HEIGHT1 - 700))
    if POSITION_PIPE1 + 80 < 0:
        CURRENT_POSITION1 = 1
        POSITION_PIPE1 = WIDTH
        X = random.choice(PIPE_TYPE_LIST)

    POSITION_PIPE2 = POSITION_PIPE2 - MOV
    CURRENT_PIPE_HEIGHT2 = HEIGHT - pipe_height + Y

    screen.blit(pipe, (POSITION_PIPE2 + WIDTH / 2, CURRENT_PIPE_HEIGHT2))
    screen.blit(flipped_pipe, (POSITION_PIPE2 + WIDTH / 2, CURRENT_PIPE_HEIGHT2 - 700))
    if POSITION_PIPE2 + WIDTH / 2 + 80 < 0:
        CURRENT_POSITION2 = 1
        POSITION_PIPE2 = WIDTH
        Y = random.choice(PIPE_TYPE_LIST)
    '''
    BIRD
    '''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bird_vel = FLAP_STRENGTH

    bird_vel += GRAVITY
    bird_y += bird_vel

    if bird_y < 0:
        bird_y = 0
        bird_vel = 0
    if bird_y + 50 > HEIGHT - ground_height:  # stop at ground
        bird_y = HEIGHT - ground_height - 50
        bird_vel = 0
    screen.blit(bird, (bird_x, bird_y))
    '''
    FLAP
    '''
    if time_ < 10:
        screen.blit(bird_u, (bird_x, bird_y))
    else:
        screen.blit(bird_d, (bird_x, bird_y))
        time_ = 0
    time_ = time_ + 1
    SCORE = SCORE + 0.01
    text_surface = font.render(f" SCORE : {int(SCORE)}", True, (0, 0, 0))
    screen.blit(text_surface, (60, 50))

    '''
    COLLISIONS
    '''
    bird_rect = pygame.Rect(bird_x, bird_y, 50, 50)

    bird_rect.y = bird_y

    pipe1_rect = pygame.Rect(POSITION_PIPE1, CURRENT_PIPE_HEIGHT1, PIPE_WIDTH, PIPE_HEIGHT)
    pipe1_top_rect = pygame.Rect(POSITION_PIPE1, CURRENT_PIPE_HEIGHT1 - 700, PIPE_WIDTH, PIPE_HEIGHT)

    pipe2_rect = pygame.Rect(POSITION_PIPE2 + WIDTH // 2, CURRENT_PIPE_HEIGHT2, PIPE_WIDTH, PIPE_HEIGHT)
    pipe2_top_rect = pygame.Rect(POSITION_PIPE2 + WIDTH // 2, CURRENT_PIPE_HEIGHT2 - 700, PIPE_WIDTH, PIPE_HEIGHT)

    if (bird_rect.colliderect(pipe1_rect) or bird_rect.colliderect(pipe1_top_rect) or bird_rect.colliderect(
            pipe2_rect) or
            bird_rect.colliderect(pipe2_top_rect)):
        GAME_OVER(SCORE)
    pygame.display.flip()
pygame.quit()
sys.exit()



# MIT License

# Copyright (c) 2025 CHAPPIE

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

