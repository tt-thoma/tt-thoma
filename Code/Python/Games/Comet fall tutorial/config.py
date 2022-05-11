import pygame
from math import ceil
from random import randint


# # Global

# screen
resolution = (1000, 720)
floor = 500

# font
score_font_name = "Bahnschrift"
score_font_size = 50
score_font_color = (0, 0, 0)

custom_font = True  # change it if you've set an already installed font
custom_font_path = "assets/custom_font.ttf"

# animation
FPS = 120
animation_speed = 55
animation_slowing_sprites = ["mummy", "alien"]


# # Player
player_health = 100
player_attack = 10
player_speed = 3

player_health_bar_color = (111, 210, 46)
player_health_bar_color_back = (221, 30, 13)
player_health_bar_height = 7

# projectile
projectile_speed = 5
projectile_rotation_speed = 2


# # Comet event

# comet
comet_damage = 20

comet_bar_height = 10
comet_bar_speed = 5
comet_bar_color = (187, 11, 11)
comet_back_bar_color = (0, 0, 0)


# # Monsters
monster_count = 2  # count of each type of monsters (eg: 2 -> 3-4 monsters)
monster_attack = 0.3

monster_health_bar_color = (211, 121, 38)
monster_health_bar_color_back = (60, 63, 60)
monster_health_bar_height = 5

"""
Death points:
When the monster is killed, this is adding to the score
"""

# mummy
mummy_death_points = 20
mummy_health = 100
mummy_speed = 3

# alien
alien_death_points = 45
alien_health = 250
alien_attack = 0.8
alien_speed = 1
alien_spawn_chance = 30  # bigger it is, rarest it is (0 is for always spawn)


# # Experimental/Coding utility
# DO NOT TOUCH IF YOU DON'T KNOW WHAT YOU ARE DOING

# aliases

# Sprite = pygame.sprite.Sprite
disp = pygame.display
img = pygame.image
load = img.load
event = pygame.event
refresh = disp.flip
window = disp.set_mode(resolution)
insert = window.blit

# functions

def roundplus(number: float):
    floatbase = number
    while floatbase > 0.999:
        floatbase -= 1
        floatbase = ceil(floatbase)
    if floatbase == 0.5:
        return ceil(number)
    else:
        return round(number)
