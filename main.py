import pygame as pg

from game.scenes.game import Game

class Main:
    
    def __init__(self, size_x, size_y, title):
        
        pg.init()
        pg.mixer.init()
        
        self.window = pg.display.set_mode([size_x, size_y])
        self.title = pg.display.set_caption(title)
        self.loop = True
        self.fps = pg.time.Clock()
        
        self.game_scene = Game()
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.loop = False
                
            self.game_scene.player.events(event)
                
    def draw(self):        
        self.game_scene.draw(self.window)
        self.game_scene.update()
                
    def run(self):
        while self.loop:
            self.fps.tick(30)
            self.draw()
            self.events()
            pg.display.update()


game = Main(1280, 720, "Platform")
game.run()