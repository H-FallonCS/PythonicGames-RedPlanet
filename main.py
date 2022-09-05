from turtle import width
import pygame

pygame.init()

#screen variables
WIDTH = 700
HEIGHT = 700

FPS = 60

#colors
RED = (223,26,26)
BLACK = (0,0,0)
WHITE = (255,255,255)

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Planet")
pygame.mouse.set_visible(False)



class Player:

    def __init__(self,x,y,size,color):
        self.x,self.y = pygame.mouse.get_pos()
        self.size = size
        self.color = color

        self.texture = pygame.image.load('planet.png')
        self.texture = pygame.transform.scale(self.texture,(self.size,self.size))


    def move(self):
        mouse_pos = pygame.mouse.get_pos()

        self.x = mouse_pos[0]-25
        self.y = mouse_pos[1]-25

    def draw(self):
        self.move()

        win.blit(self.texture,(self.x,self.y))

#this class will set up the asteroids that will try to hurt the player
class Asteroid:

    def __init__(self):
        #load the textures
        self.texture = pygame.image.load('asteroid.png')
        self.texture = pygame.transform.scale(self.texture,(30,30))

        #have an x_direction that the asteroid will go and a y_direction
        self.x_dir = 0
        self.y_dir = 0
    def move(self):
        speed =2

        print(self.x)

        if self.x <= -30:
            self.x_dir = speed
        elif self.x >= 730:
            self.x_dir = -speed
        

        self.x += self.x_dir

    def draw(self):

        self.move()
        win.blit(self.texture,(self.x,self.y))

    def spawn(self):

        self.x = -30
        self.y = 350
    

def draw():
    win.fill(WHITE)

    player.draw()
    asteroid.draw()

    pygame.display.update()


clock = pygame.time.Clock()

player = Player(250,250,50,RED)
asteroid = Asteroid()

asteroid.spawn()

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
