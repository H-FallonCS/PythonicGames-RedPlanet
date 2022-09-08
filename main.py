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

#this list will hold all the asteroid abjects
asteroids = []

#create the window
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Planet")
pygame.mouse.set_visible(False)


#this will be the Player object, the red planet
class Player:

    #start with an x,y,size, and color, set the PLayer to the mouse, grab the texture
    def __init__(self,x,y,size,color):
        self.x,self.y = pygame.mouse.get_pos()
        self.size = size
        self.color = color

        self.texture = pygame.image.load('planet.png')
        self.texture = pygame.transform.scale(self.texture,(self.size,self.size))

    #set the x and y of the player to the x and y of the mouse
    def move(self):
        mouse_pos = pygame.mouse.get_pos()

        self.x = mouse_pos[0]-25
        self.y = mouse_pos[1]-25

  #update the player then draw it to the screen
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

        #spawn the asteroids each time the function is called
        self.spawn()

    #move the asteroid by ading the direction it should be going to the x and y 
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

        #give a random speed for the objects to move
        y_speed = random.randint(1,3)

        #depending on where the astroids spawn, have them go up or down
        if self.y <= -30:
            self.y_dir = y_speed
        elif self.y >= 365:
            self.y_dir = -y_speed
        elif self.y <= 365:
            self.y_dir = y_speed
        elif self.y >= 730:
            self.y_dir = -y_speed

  #draw the asteroids by calling the move method and then blitting the asteroid to the screen
    def draw(self):

        self.move()
        win.blit(self.texture,(self.x,self.y))
        

    #will spawn the asteroids at certain spots
    def spawn(self):

        """this is probably a bad idea, but the point is to get a two option number, which we can then use to determine what side the asteroid will spawn"""
        num = random.randint(0,1)
        
        #left side
        if num == 0:
            self.x = random.randint(-50,-30)
        #right side
        if num == 1:
            self.x = random.randint(730,750)

        #set random y position
        self.y = random.randint(0,730)

        #set the directions of the asteroid
        self.set_vel()

#this function will create a certain number of asteroids and add it to a list
def create_asteroids(num_of_asteroids):

    for x in range(num_of_asteroids):
        asteroids.append(Asteroid())

#after 10 seconds, delete all asteroids inside the asteroids list
def delete_asteroids():
    global start_ticks
    seconds=(pygame.time.get_ticks()-start_ticks)/1000

    if seconds >= 10:
        for asteroid in asteroids:
            index = asteroids.index(asteroid)
            asteroids.pop()

#start the timer, then call the function to create all the asteroids
def start_wave(num_of_asteroids):
    global start_ticks
    start_ticks=pygame.time.get_ticks() 

    create_asteroids(num_of_asteroids)


    

#this will be for drawing each wave when needed
def draw_wave():
    win.fill(WHITE)

    player.draw()
    for asteroid in asteroids:
        asteroid.draw()
    delete_asteroids()
    pygame.display.update()

#check if asteroids is empty and return value
def return_empty_asteroids():
    if len(asteroids) == 0:
        return True
    else:
        return False

clock = pygame.time.Clock()


player = Player(250,250,50,RED)

#this will keep track of the rounds gone by
round = 0

#main loop
run = True
while run:

    #if no asteroids are created, start new wave
    if return_empty_asteroids():
        start_wave(20)

    print(return_empty_asteroids())

    #draw the wave
    draw_wave()

    clock.tick(FPS)

    #if X button is clicked or ESC is pressed, close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
