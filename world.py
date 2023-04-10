import pygame, pygame.freetype 
from pygame import mixer
import time
import os
from pygame.locals import *
pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 1024)
screen_width, screen_height = 1200 , 650
screen = pygame.display.set_mode((screen_width, screen_height)) 
coordinates = {
    "xc":64,
    "yc":415
    }

width, height, vel, jumpvel = 30 , 60 , 6.5, 18
obst_width, obst_height = 80, 90
ox , oy = 800 , 500
run = True
obst_list = [[800, 500, 80, 70], [100, 300, 30, 70]]
#my idea is to make every obstacle coordinates stored in a list then check if this coodinate in list
direction = 0
minion1_image = pygame.image.load(os.path.join("images/hezbminion1.png"))
minion_anim_1 = pygame.transform.scale(minion1_image, (60, 55.375))
minion2_image = pygame.image.load(os.path.join("images/hezbminion2.png"))
minion_anim_2 = pygame.transform.scale(minion2_image, (60, 55.375))
minion_animation = [minion_anim_1, minion_anim_2]

dahyeman1_image = pygame.image.load(os.path.join("images/dahyeman1.png"))
dahyeman1 = pygame.transform.scale(dahyeman1_image, (65, 60.45))
dahyeman2_image = pygame.image.load(os.path.join("images/dahyeman2.png"))
dahyeman2 = pygame.transform.scale(dahyeman2_image, (65, 60.45))
dahyeman3_image = pygame.image.load(os.path.join("images/dahyeman3.png"))
dahyeman3 = pygame.transform.scale(dahyeman3_image, (65, 60.45))
dahyeman4_image = pygame.image.load(os.path.join("images/dahyeman4.png"))
dahyeman4 = pygame.transform.scale(dahyeman4_image, (72, 66.45))
walking_list = [dahyeman4, dahyeman1, dahyeman2, dahyeman3]
walk_animation_index = 0
walking = False
#vid = Video("videos/STARTPRESS.mp4")
#vid.set_size((screen_width, screen_height))

#def intro():
    #while True:
    #    vid.draw(screen, (0,0))
    #    pygame.display.update()
    #    for event in pygame.event.get():
    #        if event.type==pygame.KEYDOWN:
    #            vid.close()

def check_x_coords(x, list):
    for i in list:
        c = i[0]
        if c-width==x or x ==c+i[2]:
            return False
        return True
def check_y_coords(y, list):
    for i in list:
        c = i[1]
        if  c-height==y or y == c+i[3]:
            return False
        return True

screen_width = 1000
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Dahye Run')
pygame.display.set_icon(pygame.image.load("images/hezbminion1.png"))

tile_size = 30
bg_img = pygame.image.load('images/background.png')


class World:
	def __init__(self, data):
		self.tile_list = []

		#load images
		brick = pygame.image.load('images/brick.png')

		row_count = 0
		for r in data:
			col_count = 0
			for c in r:
				if c == 1 or c == 2:
					img = pygame.transform.scale(brick, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					c = (img, img_rect)
					self.tile_list.append(c)
				
				col_count += 1
			row_count += 1

	def draw(self):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])

world_data = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
world = World(world_data)

class Enemy:
    def __init__(self, type):
        if type=="minion":
            self.image = minion_animation
        elif type=="harake":
            pass 
        self.width = self.image[0].get_width()
        self.height = self.image[0].get_height()
    
    def draw_enemy(self, coords):
        self.rect = pygame.Rect(coords[0], coords[1], self.image[0].get_width(), self.image[0].get_height())
        screen.blit(self.image[0], coords)

class Player:
    def __init__(self, anim_list):
        self.animation = anim_list
        self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height())
    
    def draw_player(self):
        screen.blit(self.animation[walk_animation_index], (self.player_rect.x, self.player_rect.y))
        #pygame.draw.rect(screen, (255,0,0), (coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height()), 50)

    def jump(self, keys, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                screen.blit(bg_img, (0, 0))
                minion1.draw_enemy((500, 425))
                minion2.draw_enemy((700, 335))
                world.draw()
                
                for i in range(5):
                    if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width<860:
                        coordinates["xc"] += vel
                    if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]>0:
                        coordinates["xc"] -= vel
                    coordinates["yc"] -= jumpvel
                    pygame.draw.rect(screen, (0, 0, 255), (obst_list[0][0], obst_list[0][1],obst_list[0][2],obst_list[0][3]))
                    self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height())
                    screen.blit(self.animation[walk_animation_index], (self.player_rect.x, self.player_rect.y))
                    pygame.display.update()
                    screen.blit(bg_img, (0, 0))
                    world.draw()
                    minion1.draw_enemy((500, 425))
                    minion2.draw_enemy((700, 335))
                    time.sleep(0.04)
            
                for i in range(5):
                    keys = pygame.key.get_pressed()
                    if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width<860:
                        coordinates["xc"] += vel
                    if ((keys[pygame.K_a]) or (keys[pygame.K_LEFT]))  and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]>0:
                        coordinates["xc"] -= vel
                    if (coordinates["yc"] + jumpvel) == oy or (coordinates["yc"] - jumpvel) == oy:
                        break
                    coordinates["yc"]+= jumpvel
                    pygame.draw.rect(screen, (0, 0, 255), (ox, oy, obst_width, 70))
                    self.player_rect = pygame.Rect(coordinates["xc"], coordinates["yc"], self.animation[walk_animation_index].get_width(), self.animation[walk_animation_index].get_height())
                    screen.blit(self.animation[walk_animation_index], (self.player_rect.x, self.player_rect.y))
                    pygame.display.update()
                    screen.blit(bg_img, (0, 0))
                    world.draw()
                    minion1.draw_enemy((500, 425))
                    minion2.draw_enemy((700, 335))
                    time.sleep(0.04)

    def mov(self, keys):
        global walk_animation_index, walking
        if ((keys[pygame.K_d]) or (keys[pygame.K_RIGHT])) and check_x_coords(coordinates["xc"]+vel, obst_list) is True and coordinates["xc"]-self.player_rect.width<860:
            coordinates["xc"] += vel
            if walk_animation_index+1<len(self.animation):
                walking = True
                walk_animation_index += 1
                time.sleep(0.06)
            else:
                 walk_animation_index = 0
        elif ((keys[pygame.K_a]) or (keys[pygame.K_LEFT])) and check_x_coords(coordinates["xc"]-vel, obst_list) is True and coordinates["xc"]>0:
            coordinates["xc"] -= vel
            if walk_animation_index+1<len(self.animation):
                walking = True
                walk_animation_index += 1
                time.sleep(0.06)
            else:
                 walk_animation_index = 0
        else:
            walking = False

    def get_rect(self):
         return self.player_rect.x, self.player_rect.y, self.player_rect.width, self.player_rect.height
    

run = True

mixer.music.load("sound_effects/overworld_theme.mp3")
mixer.music.play(-1)
#intro()

#MAIN LOOP
while run:
    minion1 = Enemy("minion")
    minion2 = Enemy("minion")
    dahyeman = Player(walking_list)
    keys = pygame.key.get_pressed()
    pygame.time.delay(10)
    world.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        dahyeman.jump(keys, event) #jumping
    if not walking:
        walk_animation_index = 0
    keys = pygame.key.get_pressed() 
    dahyeman.mov(keys)
    minion1.draw_enemy((500, 425))
    minion2.draw_enemy((700, 335))
    dahyeman.draw_player()
    pygame.display.update()
    screen.blit(bg_img, (0, 0))

pygame.quit()