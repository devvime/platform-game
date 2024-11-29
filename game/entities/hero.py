import pygame as pg
from game.core.entity import Entity

class Hero(Entity):

    def __init__(self, img, x, y, *groups):
        super().__init__(img, x, y, *groups)
        
        self.velocity = 4
        self.grav = 1
        
        self.left = False
        self.right = False
        self.jump = False
        
        self.ticks = 0        
        self.frame = 0
        
        self.crystals = 0
        self.lifes = 3
        
    def update(self):
        self.gravity()
        self.movement()
        self.drop()
    
    def gravity(self):
        self.velocity += self.grav
        self.rect[1] += self.velocity
        
        if self.velocity >= 10:
            self.velocity = 10
            
    def collisions(self, group=None, kill=False, name=""):        
        collison = pg.sprite.spritecollide(self, group, kill)
        
        if collison and name == "platform":
            if self.rect.y + 50 < collison[0].rect.top:
                if self.rect.left + 30 <= collison[0].rect.right:
                    if self.rect.right - 30 >= collison[0].rect.left:
                        self.rect.bottom = collison[0].rect.top
            
        if collison and name == "crystal":
            self.crystals += 1
            
        if collison and name == "enemy":
            if self.rect.y + 90 < collison[0].rect.top:
                self.velocity *= -1
                collison[0].kill()
            else:
                self.velocity *= -1
                self.lifes -= 1
                collison[0].kill()
            
    def events(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                self.right = True
            elif event.key == pg.K_a:
                self.left = True
            elif event.key == pg.K_SPACE:
                self.jump = True
                self.velocity *= -1.5
        
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                self.right = False
            elif event.key == pg.K_a:
                self.left = False
            elif event.key == pg.K_SPACE:
                self.jump = False
                
    def movement(self):
        if self.left:
            self.rect[0] -= 8
            self.anim("walk", 4, 3)
            self.image = pg.transform.flip(self.image, True, False)
        elif self.right:
            self.rect[0] += 8
            self.anim("walk", 4, 3)
            self.image = pg.transform.flip(self.image, False, False)
        else:
            self.anim("idle", 4, 3)
            
    def drop(self):
        if self.lifes > 0:
            if self.rect.y > 720:
                self.rect.x = 100
                self.rect.y = 250
                self.lifes -= 1