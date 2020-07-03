# Capstone Task
# In this program the aim is to hit the little space alien and therefore winning the game
# I want to improve this game more in future 

import pygame
import random

# Setting width and height of screen
WIDTH = 800
HEIGHT = 600 
FPS = 60

# Define colours 
WHITE = (255, 255,255)
BLACK = (0, 0,0)
RED = (255,0 ,0)
GREEN = (0, 255,0)
BLUE = (0, 0, 255)

# Initializing pygame created a window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The destroyer")
clock = pygame.time.Clock()

# Created player enemy and prize classes and defined there functions
class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 1
        self.speedx = 0
        self.speedy = 0
  
    def update(self):
       self.speedx = 0
       self.speedy = 0
       keystate = pygame.key.get_pressed()
       if keystate[pygame.K_LEFT]:
           self.speedx = -5
       if keystate[pygame.K_RIGHT]:
            self.speedx = 5
       if keystate[pygame.K_UP]:
           self.speedy = -5
       if keystate[pygame.K_DOWN]:
           self.speedy = 5
       self.rect.x += self.speedx
       self.rect.y += self.speedy
       if self.rect.right > WIDTH:
           self.rect.right = WIDTH
       if self.rect.left < 0:
            self.rect.left = 0
       if self.rect.top < 0:
           self.rect.top = 0 
       if self.rect.bottom > HEIGHT:
           self.rect.bottom = HEIGHT 
    
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png").convert()
        self.rect = self.image.get_rect() 
        self.rect.y = random.randrange(HEIGHT - self.rect.height)     
        self.rect.x = random.randrange(-100, -40)    
        self.speedy = random.randrange(1, 6)
        
    
    def update(self):
        self.rect.x += self.speedy
        if self.rect.left > WIDTH + 10:
            self.rect.y = random.randrange(HEIGHT - self.rect.height)     
            self.rect.x = random.randrange(-100, -40)    
            self.speedy = random.randrange(1, 6)
            
class Prize(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("prize.png").convert()
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(HEIGHT - self.rect.height)     
        self.rect.x = random.randrange(-100, -40)    
        self.speedy = random.randrange(1, 6)
        
    def update(self):
        self.rect.x += self.speedy
        if self.rect.left > WIDTH + 10:
            self.rect.y = random.randrange(HEIGHT - self.rect.height)     
            self.rect.x = random.randrange(-100, -40)    
            self.speedy = random.randrange(1, 6)

# Initialize pygame and create window
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
prize = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(3):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
for i in range(2):
    e = Prize()
    all_sprites.add(e)
    prize.add(e)

# Game loop
running = True
while running:
    # Keeps loop running at right speed
    clock.tick(FPS)
    # Process input events
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
     
    all_sprites.update()
    
    # Check to see if mob hit the player and print you win or you loose
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False
        print("You lose") 
    prize_hit = pygame.sprite.spritecollide(player, prize, False)
    if prize_hit:
        running = False 
        print("You win")   
    # Filled screen with black colour
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    pygame.display.flip()
# End game loop 
pygame.quit()   
