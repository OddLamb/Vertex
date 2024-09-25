# importing packages :3
import pygame as pg
import math, os, json
import numpy as np
# and the macros
from classes.settings import *
# class polygon
class Polygon():
    def __init__(self,surface):
        try:
            # checking if json file exists
            if os.path.isfile("data.json"):
                with open("data.json", 'r') as openfile:
                    # if yes, load the storaged data
                    self.verts = json.load(openfile)["polygon"]["verts"]
            else:
                # if no set the data manually
                self.verts = []
        except:
            # if no set the data manually
            self.verts = []
        self.selected_vert = None
        self.surface = surface
    def get_distance(self,p1=tuple,p2=tuple):
        # picking the two points
        x1,y1,x2,y2 = p1[0],p1[1],p2[0],p2[1]
        # calculating the distance between these two points
        # d = √((x2-x1)²+(y2-y1)²)
        return math.sqrt((x1 - x2)**2+(y1 - y2)**2)
    def angle_inbetween(self,points=list):
        # calculating the angle between three Vectors by dot product :3
        ba: vec = points[0] - points[1]
        bc: vec = points[2] - points[1]
        dot_product = np.dot(ba, bc)
        # getting the cossine of the angle
        cos_theta = dot_product / (ba.magnitude() * bc.magnitude())
        # and getting the actuall angle
        theta = math.degrees(math.acos(cos_theta))
        # returning the angle
        return min(theta, 360 - theta)
    def get_centroid(self):
        # getting the centroid of the polygon, by arithmetic average
        cx, cy = 0,0
        for pos in self.verts:
            cx+=pos[0]
            cy+=pos[1]
        return (cx/len(self.verts),cy/len(self.verts))
    def draw(self,gui_object=object):
        mpos = pg.mouse.get_pos()
        if self.selected_vert != None:
            if self.selected_vert < len(self.verts) and self.selected_vert >= 0:
                # changing the position of the selected vertice by the mouse position
                if not gui_object.snap:
                    self.verts[self.selected_vert] = mpos
                else:
                    self.verts[self.selected_vert] = ((round(mpos[0] / 32)) * 32 + 16,(round(mpos[1] / 32)) * 32 + 16)
            else:
                self.selected_vert = None
        # drawing the shape
        if len(self.verts) >= 2:
            pg.draw.polygon(self.surface,"white",self.verts,2)

            center = self.get_centroid()
            pg.draw.line(self.surface,"red",(center[0]-8,center[1]-8),(center[0]+8,center[1]+8))
            pg.draw.line(self.surface,"red",(center[0]-8,center[1]+8),(center[0]+8,center[1]-8))
        # loop passing through all the vertices
        for i in range(len(self.verts)):
            if i == len(self.verts)-1:
                # if is the last vertice, the color will be green
                col = "green"
            else:
                # if not, is red
                col = "red"
            # drawing the vertice
            pg.draw.circle(self.surface,col,self.verts[i],5)
            x,y = self.verts[i][0],self.verts[i][1]
            # enumerating the vertice (A, B, C, D...)
            text = font.render(ABC[i],True,"yellow")
        
            self.surface.blit(text,(x,y+font.get_height()/2))
            # checking if the "Show Coordinates" is on
            if gui_object.show_coordinates:
                # if so, draw the coordinates of the vertice (x = <posx>,y = <posy>)
                text = font.render("x = "+str(x)+",y = "+str(y),True,"yellow")
                rect = text.get_rect()
                # adjusting so the text will not be outside the window
                if y-font.get_height()*1.5 <= 0:
                    ty = y+font.get_height()*2
                else:
                    ty = y-font.get_height()
                if x-text.get_width()/2 <= 0:
                    tx = x+text.get_width()/2
                elif x+text.get_width()/2 >= self.surface.get_width():
                    tx = x-text.get_width()/2
                else:
                    tx = x
                rect.center = (tx,ty)
                self.surface.blit(text,rect)
        # check if the number of vertices is greater than 3, and if "Show Angles" is on
        if len(self.verts) > 2 and gui_object.show_angles:
           # loop passing through all the vertices
            for i in range(len(self.verts)):
                v = self.verts
                p2 = self.verts[i]
                # picking the three vertices nearest to the current vertice 
                if i == 0:
                    p1 = v[i+1]
                    p3 = v[len(self.verts)-1]
                elif i == len(self.verts)-1:
                    p1 = v[0]
                    p3 = v[i-1]
                else:
                    p1 = v[i+1]
                    p3 = v[i-1]
                # calculating the angle between the three by dot product
                text = font.render("error",True,"purple")
                try:
                    if (self.get_distance(p2,p1) != 0 and self.get_distance(p2,p3) != 0 and self.get_distance(p1,p3) != 0):
                        angle = self.angle_inbetween([vec(p1[0],p1[1]),vec(p2[0],p2[1]),vec(p3[0],p3[1])])
                        # rounding or not, based on the "Round" option
                        if gui_object.round:
                            text = font.render(str(round(angle))+"°",True,"purple")
                        else:
                            text = font.render(str(angle)+"°",True,"purple")
                except:
                    pass
                pos = text.get_rect()
                # picking the center of the polygon
                cx,cy,t = self.get_centroid()[0],self.get_centroid()[1], font.get_height()
                # adjusting so the angle text will be pointing to the center
                if cx > p2[0]:
                    tx = p2[0]+t/2
                else:
                    tx = p2[0]-t/2
                
                if cy > p2[1]:
                    ty = p2[1]+t/2
                else:
                    ty = p2[1]-t/2
                pos.center = (tx,ty)
                
                pg.draw.rect(self.surface,"white",pos)
                self.surface.blit(text,pos)
        # checking if the number of vertices is greater than 1
        if len(self.verts) > 1:
            # loop passing through all the vertices
            for i in range(len(self.verts)):
                # picking two vertices
                if i>=1:
                    x1,y1,x2,y2 = self.verts[i-1][0],self.verts[i-1][1],self.verts[i][0],self.verts[i][1]     
                else:
                    x1,y1,x2,y2 = self.verts[0][0],self.verts[0][1],self.verts[len(self.verts)-1][0],self.verts[len(self.verts)-1][1] 
                # calculating the distance between these two vertices
                d = self.get_distance((x1,y1),(x2,y2))
                # if the "Round" option is enable, round the result
                if gui_object.round:
                    text = font.render(str(round(d)),True,"black")
                else:
                    text = font.render(str(d),True,"black")
                
                xx,yy = (x1+x2)/2, (y1+y2)/2
                pos = text.get_rect()
                # adjusting so the text will not be outside the window
                if yy-font.get_height()*1.5 <= 0:
                    ty = yy+font.get_height()/2
                else:
                    ty = yy
                if xx-text.get_width()/2 <= 0:
                    tx = xx+text.get_width()/2
                elif xx+text.get_width()/2 >= self.surface.get_width():
                    tx = xx-text.get_width()/2
                else:
                    tx = xx
                pos.center = (tx,ty)
                    
                pg.draw.rect(self.surface,"white",pos)
                self.surface.blit(text,pos)
    def input(self,e=list,gui_object=object):
        # getting the mouse position
        mpos = pg.mouse.get_pos()
        # checking if any mouse button is down
        if e.type == pg.MOUSEBUTTONDOWN:
            # checking if that button is the right button of the mouse
            if pg.mouse.get_pressed()[2]:
                # checking if any vertice is selected
                if self.selected_vert == None:
                    # loop passing through all the vertices, checking if any is colliding with the cursor
                    for i in range(len(self.verts)):
                        x,y,t = self.verts[i][0],self.verts[i][1],10
                        r = pg.rect.Rect(x-t/2,y-t/2,t,t)
                        if r.collidepoint(mpos[0],mpos[1]):
                            # if is colliding, storing the index of the vertice
                            self.selected_vert = i
            # checking if that button is the right button of the mouse
            elif pg.mouse.get_pressed()[0] and len(self.verts) < len(ABC):
                # creating another vertice
                if not gui_object.snap:
                    self.verts.append(mpos)
                else:
                    self.verts.append(((round(mpos[0] / 32)) * 32 + 16,(round(mpos[1] / 32)) * 32 + 16))
        # checking if any mouse button is down
        elif e.type == pg.MOUSEBUTTONUP:
            if self.selected_vert != None:
                self.selected_vert = None