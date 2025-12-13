import pygame 
import sys
import random
import math

def random_check():
    check = []
    counter = 0
    while check.count(0) < 10 :
        check = []
        for i in range(10):
            ran1 = random.randint(1,2)
            ran2 = random.randint(1,2)
            if ran1 == ran2:
                check.append(1)
            else:
                check.append(0)
        counter += 1
    return counter



pygame.init()

#initial variable
screen = pygame.display.set_mode((1289,720))
color = 'red'
i = 0
counter = 0
p = 0
failed_chance = 1-(0.5**10)
n_font = pygame.font.Font(None,30)
clock = pygame.time.Clock()
win_sound = pygame.mixer.Sound('Tuturu.wav')
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0
boss_hp = 1000

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                i += 1
                counter = random_check()
                p = (1-failed_chance**counter)*100
                
                if p < 10:
                    color = 'gold'
                    boss_hp -= 100
                    win_sound.play()
                else:
                    if i%2 == 0:
                        color = 'blue'
                    else:
                        color = 'green'
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
        
    screen.fill('lightblue')
    
    
    text = n_font.render(f"You have tried {counter} times to get all zero and that is {round(p,5)}% chance",True,'black')
    boss_hp_text = n_font.render(f"HP: {boss_hp}",True,'black')
    pygame.draw.circle(screen,color,player_pos,radius=30)
    pygame.draw.circle(screen,'red',(1000,350),radius=200)
    
    screen.blit(text,(50,50))
    screen.blit(boss_hp_text,(900,350))
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000

