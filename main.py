from turtle import width
import pygame

pygame.init()

#screen variables
WIDTH = 500
HEIGHT = 500

FPS = 60

#colors
RED = (223,26,26)
BLACK = (0,0,0)
WHITE = (255,255,255)

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Planet")


class Player():

    def __init__(self,x,y,size,color):
        self.x,self.y = pygame.mouse.get_pos()
        self.size = size
        self.color = color

        self.texture = pygame.image.load('planet.png')


    def move(self):
        mouse_pos = pygame.mouse.get_pos()

        self.x,self.y = mouse_pos
    
    def draw(self):
        self.move()

        win.blit(self.texture,(self.x-50,self.y-50))

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