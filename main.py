from turtle import width
import pygame

pygame.init()

#screen variables
WIDTH = 0
HEIGHT = 0

FPS = 60

#colors
RED = (223,26,26)
BLACK = (0,0,0)
WHITE = (255,255,255)

win = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Red Planet")
pygame.mouse.set_visible(False)

WIDTH, HEIGHT = win.get_size()

class Player:

    def __init__(self,x,y,size,color):
        self.x,self.y = pygame.mouse.get_pos()
        self.size = size
        self.color = color

        self.texture = pygame.image.load('planet.png')


    def move(self):
        mouse_pos = pygame.mouse.get_pos()

        self.x = mouse_pos[0]-25
        self.y = mouse_pos[1]-25

    def draw(self):
        self.move()

        win.blit(self.texture,(self.x,self.y))

class Enemy:
    pass

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
