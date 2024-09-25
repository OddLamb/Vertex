# importing packages :3
import pygame as pg
import os
# macros
WINDOW_RESOLUTION = (600,600)
FRAMERATE = 60
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vec = pg.math.Vector2
# init pg modules
pg.font.init()
pg.mixer.init()
# main font
font = pg.font.SysFont("Comic Sans",25)
# sfx
on_sfx = pg.mixer.Sound(os.path.join(os.getcwd(),"assets/sounds/on.wav"))
off_sfx = pg.mixer.Sound(os.path.join(os.getcwd(),"assets/sounds/off.wav"))
switch_sfx = pg.mixer.Sound(os.path.join(os.getcwd(),"assets/sounds/switch.wav"))
clear_sfx = pg.mixer.Sound(os.path.join(os.getcwd(),"assets/sounds/clear.wav"))