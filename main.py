# importing packages :3
import pygame as pg
# macros 
from classes.settings import *
# importing classes
from classes.polygon import *
from classes.gui import *

pg.init()
class App():
    def __init__(self):
        # setting the window and clock
        self.window = pg.display.set_mode((WINDOW_RESOLUTION),pg.RESIZABLE)
        pg.display.set_icon(pg.image.load(os.path.join(os.getcwd(),"./assets/icon.png")))
        self.clock = pg.time.Clock()
        self.running = True
        
    def update(self):
        # creating an polygon object, and a gui object
        polygon = Polygon(self.window)
        gui = Gui(self.window)
        # while loop running while the variable "running" is True
        while self.running:
            # updating the clock
            self.clock.tick(FRAMERATE)
            # showing the fps in the caption of the window
            pg.display.set_caption("Vertex")
            # for loop passing through all the pygame events
            for e in pg.event.get():
                # if the window is being closed
                if e.type == pg.QUIT:
                    self.running = False
                    # creating or overriding a json file
                    with open(os.path.join(os.getcwd(),"data.json"), "w") as file:
                        # creating a dict containing all the data that it wanna save
                        value ={
                            "settings": {
                                "round": gui.round,
                                "language": gui.language,
                                "coords": gui.show_coordinates,
                                "angle": gui.show_angles,
                                "snap": gui.snap
                            },
                            "polygon": {
                                "verts": polygon.verts
                            }
                        }
                        # saving into the json file
                        json.dump(value,file)
                        file.close()
                # running the input event in each object
                polygon.input(e,gui)
                gui.input(e,polygon)
            # filling the window in black
            self.window.fill("black") 
            # running the draw event in each object
            gui.draw(polygon)
            polygon.draw(gui)
            # updating the window
            pg.display.update()
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.update()