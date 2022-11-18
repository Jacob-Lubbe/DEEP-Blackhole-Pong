# Developer : Hamdy Abou El Anein

import random
import pygame
import sys
from pygame import *
from easygui import *

image = "/usr/share/daylight/daylightstart/DayLightLogoSunSet.gif"
msg = "                           Welcome to Daylight Pong \n\n\n Rules of Daylight Pong \n\n\n Player 1 \n\n Arrow up = UP \n Arrow down = DOWN\n\n Player 2 \n\n Z = UP \n S = Down"
choices = ["OK"]
buttonbox(msg, image=image, choices=choices)

pygame.init()
fps = pygame.time.Clock()


WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
BLACK = (24, 36, 56)


WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = [0, 0]
paddle2_vel = 0
l_score = 0
r_score = 0


window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Daylight Pong")

class background(pygame.sprite.Sprite):
	def __init__(self,image_file,location):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load(image_file)
		self.rect=self.image.get_rect()
		self.rect.left,self.rect.top=location

def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    horz = random.randrange(2, 4)
    vert = random.randrange(1, 3)

    if right == False:
        horz = -horz

    ball_vel = [horz, -vert]


def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, l_score, r_score  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
    paddle2_pos = [WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT // 2]
    l_score = 0
    r_score = 0
    if random.randrange(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)


def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score
    
    bg=background('space.png',[0,0])
    canvas.fill(WHITE)
    canvas.blit(bg.image,bg.rect)
 
##    canvas.fill(BLACK)
    ## pygame.draw.line(canvas, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
  ##  pygame.draw.line(canvas, WHITE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
   ## pygame.draw.line(
 ##       canvas, WHITE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1
 ##   )
   ## pygame.draw.circle(canvas, WHITE, [WIDTH // 2, HEIGHT // 2], 70, 1)##

    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
    	print(paddle1_pos)
    	print()
    	print(paddle1_vel)
    	print()
    	paddle1_pos[1] += paddle1_vel[1]
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel[1] > 0:
        paddle1_pos[1] += paddle1_vel[1]
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel[1] < 0:
        paddle1_pos[1] += paddle1_vel[1]
        
    if paddle1_pos[0] > HALF_PAD_WIDTH and paddle1_pos[0] < WIDTH//2 - HALF_PAD_WIDTH:
        paddle1_pos[0] += paddle1_vel[0]
    elif paddle1_pos[0] == HALF_PAD_WIDTH and paddle1_vel[0] > 0:
        paddle1_pos[0] += paddle1_vel[0]
    elif paddle1_pos[0] == WIDTH//2 - HALF_PAD_WIDTH and paddle1_vel[0] < 0:
        paddle1_pos[0] += paddle1_vel[0]

    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel
    

    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel

    def compute_distance(vec):
    	return (vec[0]**2+vec[1]**2)**.5
    def compute_dir_vec(pos1, pos2):
    	return [(pos1[0] - pos2[0]),  (pos1[1] - pos2[1])]
    def compute_force(vec1, vec2):
    	direction = compute_dir_vec(vec1, vec2)
    	
    dir1 = compute_dir_vec(ball_pos, paddle1_pos)
    dir2 = compute_dir_vec(ball_pos, paddle2_pos)
	
    r1, r2 = compute_distance(dir1),compute_distance(dir2) 
    
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    pygame.draw.circle(canvas, ORANGE, ball_pos, 20, 0)
    pygame.draw.polygon(
        canvas,
        GREEN,
        [
            [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
            [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
            [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
        ],
        0,
    )
    pygame.draw.polygon(
        canvas,
        GREEN,
        [
            [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
            [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
            [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
        ],
        0,
    )

    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(
        paddle1_pos[1] - HALF_PAD_HEIGHT, paddle1_pos[1] + HALF_PAD_HEIGHT, 1
    ):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        r_score += 1
        ball_init(True)

    if int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH and int(
        ball_pos[1]
    ) in range(paddle2_pos[1] - HALF_PAD_HEIGHT, paddle2_pos[1] + HALF_PAD_HEIGHT, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= WIDTH + 1 - BALL_RADIUS - PAD_WIDTH:
        l_score += 1
        ball_init(False)

    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score " + str(l_score), 1, (255, 255, 0))
    canvas.blit(label1, (50, 20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score " + str(r_score), 1, (255, 255, 0))
    canvas.blit(label2, (470, 20))


def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_LEFT: 
    	paddle1_vel = -8
    elif event.key == K_RIGHT: 
    	paddle1_vel = 8
    elif event.key == K_w:
        paddle1_vel[1] = -8
    elif event.key == K_s:
        paddle1_vel[1] = 8
    elif event.key == K_a: 
    	paddle1_vel[0] = -8
    elif event.key == K_d: 
    	paddle1_vel[0] = 8


def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_w, K_s,K_a,K_d):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN, K_LEFT, K_RIGHT):
        paddle2_vel = 0


init()


while True:

    draw(window)
   

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)
