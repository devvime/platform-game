import pygame as pg

class Entity(pg.sprite.Sprite):

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)
        
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        
        self.ticks = 0
        self.frame = 0
        
    def anim(self, name="", ticks=30, frames=3):
        self.ticks += 1
        if self.ticks > ticks:
            self.ticks = 0
            self.frame += 1
            
        if self.frame > frames:
            self.frame = 0
            
        self.image = pg.image.load("assets/" + name + str(self.frame) + ".png")