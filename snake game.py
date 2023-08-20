import pygame
import random
pygame.init()
#game screen
s_w = 640                                                       #width
s_h = 450                                                       #height
s = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("Snake Game")
# Colors
black = (0, 0, 0)
blue = (100, 100, 100)
green = (0, 100, 0)
red= (100, 0, 0)
# Snake properties
s_pos = [100, 40]
s_b = [[100, 40], [90, 40], [80, 40]]
s_d = 'RIGHT'
change = s_d
# Food properties
f_p = [random.randrange(1, (s_w // 20)) * 20,random.randrange(1, (s_h // 20)) * 20]
f_spawn = True
score = 0
g_o = False                                              #game over
#frames per second controller
fps = pygame.time.Clock()
while not g_o:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = 'UP'
            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change= 'RIGHT'

    #directions
    if change == 'UP' and not s_d == 'DOWN':
        s_d= 'UP'
    if change == 'DOWN' and not s_d == 'UP':
        s_d = 'DOWN'
    if change == 'LEFT' and not s_d == 'RIGHT':
        s_d = 'LEFT'
    if change == 'RIGHT' and not s_d == 'LEFT':
        s_d = 'RIGHT'

    #snake position 
    if s_d == 'RIGHT':
        s_pos[0] += 15
    if s_d == 'LEFT':
        s_pos[0] -= 10
    if s_d == 'UP':
        s_pos[1] -= 10
    if s_d == 'DOWN':
        s_pos[1] += 10

    # Snake body growing 
    s_b.insert(0, list(s_pos))
    if s_pos[0] == f_p[0] and s_pos[1] == f_p[1]:
        score += 1
        f_spawn = False
    else:
        s_b.pop()

    if not f_spawn:
        f_p = [random.randrange(1, (s_w // 15)) * 15,random.randrange(1, (s_h // 15)) * 15]
    f_spawn = True

    # Draw Snake and food
    s.fill(black)
    for pos in s_b:
        pygame.draw.rect(s, green,pygame.Rect(pos[0], pos[1], 15, 15))

    pygame.draw.rect(s, blue, pygame.Rect(f_p[0], f_p[1], 10, 10))

    # Game Over 
    if s_pos[0] < 0 or s_pos[0] > s_w-25:
        g_o = True
    if s_pos[1] < 0 or s_pos[1] > s_h-25:
        g_o = True

    # snake body
    for block in s_b[1:]:
        if s_pos[0] == block[0] and s_pos[1] == block[1]:
            g_o = True

    pygame.display.update()
    fps.tick(15)

pygame.quit()
quit()