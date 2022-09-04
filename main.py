from turtle import width
import pygame

pygame.init()

#screen variables
WIDTH = 500
HEIGHT = 500

FPS = 60

#colors
RED = (223,26,26)
WHITE = (0,0,0)

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Planet")


class Player():

    def __init__(self,x,y,size,color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color


    def move(self):
        mouse_pos = pygame.mouse.get_pos()

        self.x,self.y = mouse_pos
    
    def draw(self):
        self.move()

        pygame.draw.circle(win,self.color,(self.x,self.y),self.size,0)

def draw():
    win.fill(WHITE)

    player.draw()

    pygame.display.update()


clock = pygame.time.Clock()

player = Player(250,250,30,RED)

run = True
while run:

    draw()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False