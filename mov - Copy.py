import pygame
import pygame.freetype 
import time
import json
import os
pygame.init()
screen_width, screen_height = 1200 , 650
screen = pygame.display.set_mode((screen_width, screen_height))
coordinates = {
    "xc":500,
    "yc":500
    }
try:
    with open("coordinates.json") as coords:
        coordinates = json.load(coords)
except FileNotFoundError: 
    pass

def check_x_coords(x, list):
    for i in list:
        c = i[0]
        if c-width==x or x ==c+i[2] :
            return False
        return True
def check_y_coords(y, list):
    for i in list:
        c = i[1]
        if  c-height==y or y == c+i[3] :
            return False
        return True
    
class Player:
    def __init__(self, player_image):
        self.image = pygame.image.load(os.path.join(player_image))
        self.player1 = pygame.transform.scale(self.image, (240, 221.5))
        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.player1.get_width(), self.player1.get_height())
    def draw_player(self):
        screen.blit(self.player1, (self.player_rect.x, self.player_rect.y))
    def jump(self, keys, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                screen.fill((0,0,0))
                for i in range(5):
                        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True:
                            coordinates["xc"] += vel*3
                        if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True:
                            coordinates["xc"] -= vel*3
                        coordinates["yc"] -= jumpvel
                        pygame.draw.rect(screen, (0, 0, 255), (obst_list[0][0], obst_list[0][1],obst_list[0][2],obst_list[0][3]))
                        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.player1.get_width(), self.player1.get_height())
                        screen.blit(self.player1, (self.player_rect.x, self.player_rect.y))
                        pygame.display.update()
                        screen.fill((0, 0, 0))
                        time.sleep(0.04)
            
                for i in range(5):
                        keys = pygame.key.get_pressed()
                        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True:
                            coordinates["xc"] += vel*3
                        if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True:
                            coordinates["xc"] -= vel*3
                        if (coordinates["yc"] + jumpvel) == oy or (coordinates["yc"] - jumpvel) == oy:
                            break
                        coordinates["yc"]+= jumpvel
                        pygame.draw.rect(screen, (0, 0, 255), (ox, oy, obst_width, 70))
                        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.player1.get_width(), self.player1.get_height())
                        screen.blit(self.player1, (self.player_rect.x, self.player_rect.y))
                        pygame.display.update()
                        screen.fill((0, 0, 0))
                        time.sleep(0.04)
    def mov(self, keys):
        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True:
            coordinates["xc"] += vel
        if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]-vel, obst_list) is True:
            coordinates["xc"] -= vel

width, height, vel, jumpvel = 30 , 60 , 5, 40
obst_width, obst_height = 80, 90
ox , oy = 800 , 500
run = True
obst_list = [[800, 500, 80, 70], [100, 300, 30, 70]]
#my idea is to make every obstacle coordinates stored in a list then check if this coodinate in list
direction = 0

while run:
    larry = Player("images/normal.png")
    keys = pygame.key.get_pressed()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False #jumping
        larry.jump(keys, event)
    keys = pygame.key.get_pressed() 
    larry.mov(keys)
    pygame.draw.rect(screen, (0, 0, 255), (ox, oy, obst_width, 70))
    larry.draw_player()
    pygame.display.update()
    screen.fill((0, 0, 0))

with open("coordinates.json", "w") as coords:
    json.dump(coordinates, coords)

pygame.quit()