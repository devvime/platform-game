import pygame as pg
from game.core.entity import Entity

class Enemy(Entity):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)
        
    def update(self):
        self.anim("enemy", 4, 3)