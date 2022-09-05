import random
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
         self.x += self.x_dir
         self.y += self.y_dir

   
    #depending on which side the asteroid spawns, set it to move in one direction for the x and y cords
    def set_vel(self):     

        #if the x cord is lef then  go right, if its right then  go left
        x_speed = random.randint(1,3)
        if self.x <= -30:
            self.x_dir = x_speed
        elif self.x >= 730:
            self.x_dir = -x_speed

        y_speed = random.randint(1,3)

        #if the y cord is below the half, go up, if its above the half go down
        if self.y <= -30:
            self.y_dir = y_speed
        elif self.y >= 365:
            self.y_dir = -y_speed
        elif self.y <= 365:
            self.y_dir = y_speed
        elif self.y >= 730:
            self.y_dir = -y_speed

        
        

  

    def draw(self):

        self.move()
        win.blit(self.texture,(self.x,self.y))
        print(self.x,self.y)

    def spawn(self):

        self.x = -40
        self.y = 100
    

def draw():
    win.fill(WHITE)

    player.draw()
    asteroid.draw()

    pygame.display.update()


clock = pygame.time.Clock()

player = Player(250,250,50,RED)
asteroid = Asteroid()

asteroid.spawn()
asteroid.set_vel()

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
