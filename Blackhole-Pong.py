

import pygame
import os
from GravBody import GravBody
from constants import *

pygame.font.init()
pygame.mixer.init()


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Pong")


BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('forte', 40)
WINNER_FONT = pygame.font.SysFont('forte', 100)



#YELLOW_HIT = pygame.USEREVENT + 1
#RED_HIT = pygame.USEREVENT + 2



SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

EARTH = GravBody(
        name='Earth',
        image='Assets/Earth.png',
        scale=(125, 125), 
        vector=(580,300),
        mass=1,
        velocity=(100,0)
        )
        
player1 = GravBody(
        name='Player1',
        image='Assets/spaceship_red.png',
        scale=(125, 125), 
        vector=(100, 300),
        mass=1,
        velocity=(0,0)
        )
        
        
player2 = GravBody(
        name='Player2',
        image='Assets/spaceship_red.png',
        scale=(125, 125), 
        vector=(1055, 300),
        mass=1,
        velocity=(0,0)
        )
        
#arth.direction = 1,1 
def logistic_like_curve(nd_arr, scale = 1, mean=0):
        return 2*(1.0/(1+10**(-nd_arr/scale))-.5)*scale
        
def do_physics(timestep=1):
        '''
        update positions and compute physics
        '''
        Player1_gforce = EARTH.calc_gravity(player1)
        Player2_gforce = EARTH.calc_gravity(player2)
        force = Player2_gforce+Player1_gforce
        force = logistic_like_curve(force, scale=g_constant/5000)
        EARTH.update(timestep=timestep, force = force)
        print(EARTH.velocity)
        
        
#ef update():
    #
    # Move the ball along its current direction at its current speed
    #
  # dx, dy = earth.direction
  #earth.move_ip(earth.direction * dx, earth.speed * dy)

    #
    # Bounce the ball off the left or right walls
    #
 #  if earth.right >= WIDTH or earth.left <= 0:
  #    earth.direction = -dx, dy

    #
    # Bounce the ball off the top or bottom walls
    # (We'll remove this later when the bat and the
    # bricks are in place)
    #
#if earth.bottom >= HEIGHT or earth.top <= 0:
  #    earth.direction = dx, -dy
        
def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    
    EARTH.draw()
    player1.draw()
    player2.draw()
    pygame.display.update()
    return

    #red_health_text = HEALTH_FONT.render(
    #    "Score: " + str(red_health), 1, WHITE)
    #yellow_health_text = HEALTH_FONT.render(
    #    "Score: " + str(yellow_health), 1, WHITE)
    #WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    #WIN.blit(yellow_health_text, (10, 10))

    #WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    #WIN.blit(RED_SPACESHIP, (red.x, red.y))
    #WIN.blit(EARTH, (580,300))

    #pygame.display.update()
    

def player1_handle_movement(keys_pressed):
    if keys_pressed[pygame.K_a] and player1.vector[0] - VEL > 0:  # LEFT
        player1.vector[0] -= VEL
    if keys_pressed[pygame.K_d] and player1.vector[0] + VEL + player1.scale[0] < BORDER.x:  # RIGHT
        player1.vector[0] += VEL
    if keys_pressed[pygame.K_w] and player1.vector[1] - VEL > 0:  # UP
        player1.vector[1] -= VEL
    if keys_pressed[pygame.K_s] and player1.vector[1] + VEL + player1.scale[1] < HEIGHT - 15:  # DOWN
        player1.vector[1] += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL
        
def player2_handle_movement(keys_pressed):
    if keys_pressed[pygame.K_LEFT] and player2.vector[0] - VEL > BORDER.x + BORDER.width:  # LEFT
        player2.vector[0] -= VEL
    if keys_pressed[pygame.K_RIGHT] and player2.vector[0] + VEL + player2.scale[0] < WIDTH:  # RIGHT
        player2.vector[0] += VEL
    if keys_pressed[pygame.K_UP] and player2.vector[1] - VEL > 0:  # UP
        player2.vector[1] -= VEL
    if keys_pressed[pygame.K_DOWN] and player2.vector[1] + VEL + player2.scale[1] < HEIGHT - 15:  # DOWN
        player2.vector[1] += VEL
        


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /
                         2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(1055, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 0
    yellow_health = 0

    clock = pygame.time.Clock()
    run = True
    

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

       
        winner_text = ""
        if red_health >= 10:
            winner_text = "Left Wins!"

        if yellow_health >= 10:
            winner_text = "Right Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        player1_handle_movement(keys_pressed)
        player2_handle_movement(keys_pressed)

        #  handle_bullets(yellow_bullets, red_bullets, yellow, red)
        #move ball
        do_physics(timestep=1.0/FPS)
        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)
                    
        #ball.draw(WIN)

    main()


if __name__ == "__main__":
    main()
    

