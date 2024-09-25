# importing packages :3
import pygame as pg
import os, json
# and the macros
from classes.settings import *

class Gui():
    def __init__(self,surface=object):
        self.surface = surface
        # dictionary, containing all the button's text in English, Brazilian-Portuguese, German and Russian :)
        self.settings_text = {
            "en": ["Round","Show coordinates","Show angles","Language","Snap to grid","Clear"],
            "pt-br": ["Arredondar","Mostrar coordenadas","Mostrar Ângulos","Idioma","Alinhar à grade","Limpar"],
            "de": ["Runden","Koordinaten anzeigen","Winkel anzeigen","Sprache","Am Raster ausrichten","Zu reinigen"],
            "ru":  ["Круглый","Показать координаты","Показать ракурсы","Язык","Привязка к сетке","Чистить"]
        }
        # dictionary, containing all the polygons possibles nomenclatures in English, Brazilian-Portuguese, German and Russian :)
        self.names = {
            "en": ["","Dot","Straight segment","Triangle","Quadrilateral","Pentagon","Hexagon","Heptagon","Octagon","Nonagon","Decagon","-gon"],
            "pt-br": ["","Ponto","Segmento de Reta","Triângulo","Quadrilátero","Pentágono","Hexágono","Heptágono","Octógono","Eneágono","Decágono","-gono"],
            "de": ["", "Punkt", "Gerade", "Dreieck", "Viereck", "Fünfeck", "Sechseck", "Siebeneck", "Achteck", "Neuneck", "Zehneck", "-eck"],
            "ru": ["", "Точка", "Отрезок", "Треугольник", "Четырехугольник", "Пятиугольник", "Шестиугольник", "Семиугольник", "Восьмиугольник", "Девятиугольник", "Десятиугольник", "-угольник"]
        }
        # an list containing all the settings buttons "key" 
        self.settings = ["round","coords","angle","language","snap","clear"]
        try:
            # checking if json file exists
            if os.path.isfile("data.json"):
                with open("data.json", 'r') as openfile:
                    # if yes, load the storaged data
                    j = json.load(openfile)
                    self.round = j["settings"]["round"]
                    self.show_coordinates = j["settings"]["coords"]
                    self.language = j["settings"]["language"]
                    self.show_angles = j["settings"]["angle"]
                    self.snap = j["settings"]["snap"]
            else:
                # if no set the data manually
                self.round = True
                self.show_coordinates = True
                self.language = "en"
                self.show_angles = True
                self.snap = True
        except:
            # if no set the data manually
            self.round = True
            self.show_coordinates = True
            self.language = "en"
            self.show_angles = True
            self.snap = True
        self.selected_button = None
    def input(self,e=list,polygon_object=object):
        # getting the mouse position
        mpos = pg.mouse.get_pos()
        # checking if any mouse button is down
        if e.type == pg.MOUSEBUTTONDOWN:
            # checking if that mouse button is the right one
            if pg.mouse.get_pressed()[2]:
                # loop through all the settings buttons
                for i in range(len(self.settings)):
                    x,y = 0,i*(font.get_height())+(i*4)
                    text = font.render(self.settings_text[self.language][i],True,"black")
                    # getting a collision rectangle
                    r = text.get_rect()
                    r.topleft = (x,y)
                    # checking if the mouse is hovering that rectangle
                    if r.collidepoint(mpos[0],mpos[1]):
                        # storing the button that is being pressed, to apply a dark color to it in the draw()
                        self.selected_button = i
                        # checking the key of the button that is being pressed
                        match self.settings[i]:
                            case "round":
                                if self.round == False:
                                    # playing sound effect
                                    on_sfx.play(0)
                                else:
                                    # playing sound effect
                                    off_sfx.play(0)
                                # reversing the "round" option, if True -> False and if False -> True
                                self.round = not self.round
                                break
                            case "clear":
                                # checking if the number of vertices in the polygon is greater than 0
                                if len(polygon_object.verts) > 0:
                                    # playing sound effect
                                    clear_sfx.play(0)
                                    # and erasing all the vertices
                                    polygon_object.verts = []
                                break
                            case "coords":
                                if self.show_coordinates == False:
                                    # playing sound effect
                                    on_sfx.play(0)
                                else:
                                    # playing sound effect
                                    off_sfx.play(0)
                                # reversing the "show_coordinates" option, if True -> False and if False -> True
                                self.show_coordinates = not self.show_coordinates
                                break
                            case "snap":
                                if self.snap == False:
                                    # playing sound effect
                                    on_sfx.play(0)
                                else:
                                    # playing sound effect
                                    off_sfx.play(0)
                                # reversing the "snap" option, if True -> False and if False -> True
                                self.snap = not self.snap
                                break
                            case "language":
                                # playing sound effect
                                switch_sfx.play(0)
                                match self.language:
                                    # switching the language in a cyclic pathern
                                    case "en":
                                        self.language = "pt-br"
                                        break
                                    case "pt-br":
                                        self.language = "de"
                                        break
                                    case "de":
                                        self.language = "ru"
                                        break
                                    case "ru":
                                        self.language = "en"
                                        break
                                break
                            case "angle":
                                if self.show_angles == False:
                                    # playing sound effect
                                    on_sfx.play(0)
                                else:
                                    # playing sound effect
                                    off_sfx.play(0)
                                # reversing the "show_angles" option, if True -> False and if False -> True
                                self.show_angles = not self.show_angles
                                break
        # checking if any mouse button is up
        elif e.type == pg.MOUSEBUTTONUP:
            # if the button is previosly stored then reset it
            if self.selected_button != None:
                self.selected_button = None
    def draw(self,polygon_object=object):
            t = 32
            # drawing the lines pathern background
            for x in range(round(self.surface.get_width()/t)):
                for y in range(round(self.surface.get_height()/t)):
                    x1 = x*t
                    x2 = x*t
                    y1 = y*t
                    y2 = y*t
                    pg.draw.line(self.surface,(16,16,16),(0,y1),(self.surface.get_width(),y2),2)
                    pg.draw.line(self.surface,(16,16,16),(x1,0),(x2,self.surface.get_height()),2)
            # picking the actuall language selected
            s = self.names[self.language]
            # checking if the number of vertices in the polygon is greater than 10
            if len(polygon_object.verts) < len(s)-1:
                # if yes, name it based on <number of vertices>-gon 
                text = font.render(s[len(polygon_object.verts)],True,"black")
            else:
                # if no, name it based on the dictionary >:3
                text = font.render(f"{len(polygon_object.verts)}{s[len(s)-1]}",True,"black")
            # picking a rectangle in the wid and hei of the text
            r = text.get_rect()
            # setting its origin to top-center
            r.centerx = WINDOW_RESOLUTION[0]/2
            pg.draw.rect(self.surface,"white",r)
            # drawing the resulting text 
            self.surface.blit(text,r)
            # loading a icon based on the language
            flag = pg.image.load(os.path.join(os.getcwd(),f"assets/icons/{self.language}.png"))
            # drawing it
            self.surface.blit(flag,(self.surface.get_width()-flag.get_width(),0))
            # loop through all the settings buttons
            for i in range(len(self.settings)):  
                x,y = 0,i*(font.get_height())+(i*4)
                if self.selected_button == i:
                    # if the value stored in the "selected_button" variable equals on the current index, the change its color to a darker one
                    button_color = "gray"
                else:
                    # if no keep the default one
                    button_color = "white"
                # loading the text translated, based on the key stored on the current index
                text = font.render(self.settings_text[self.language][i],True,"black")
                r = text.get_rect()
                # aligning the text to top-left 
                r.topleft = (x,y)
                # and drawing it all
                pg.draw.rect(self.surface,button_color,r)
                self.surface.blit(text,(x,y))
