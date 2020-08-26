import pygame
import random
import sys 
pygame.init()
clock = pygame.time.Clock()
screen_wide = 1200
screen_height = 500
bg_color = (255,200,200)
player_colour = (0,255,0)

screen = pygame.display.set_mode((screen_wide,screen_height))
pygame.display.set_caption("pong")
ball = pygame.Rect(screen_wide//2-15,screen_height//2-15,30,30)
player = pygame.Rect(1180,screen_height//2-70,10,140)
opponent = pygame.Rect(10,screen_height//2-70,10,140)



ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7             
    player.y+= player_speed
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0  or ball.right >= screen_wide:
        ball_restart()
    if ball.colliderect(player or ball.colliderect(opponent)):
        ball_speed_x *= -1
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

    def ball_restart():
        global ball_speed_y ,ball_speed_x
        ball.center = (screen_height//2,screen_height//2)
        ball_speed_y *= random.choice((1,-1))
        ball_speed_x *= random.choice((1,-1))
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),player)
    pygame.draw.rect(screen,(255,255,255),opponent)
    pygame.draw.rect(screen,(255,255,255),ball)
    pygame.display.flip()
    clock.tick(60)