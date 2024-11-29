import pygame as pg
from game.core.entity import Entity
from game.entities.hero import Hero
from game.entities.enemy import Enemy

class Game:
    
    def __init__(self):
        
        self.all_sprites_group = pg.sprite.Group()
        self.all_plattform_group = pg.sprite.Group()
        self.cristal_group = pg.sprite.Group()
        self.enemy_group = pg.sprite.Group()
        
        self.bg = Entity("assets/bg.png", 0, 0, self.all_sprites_group)
        
        self.tree1 = Entity("assets/tree1.png", 80, 250, self.all_sprites_group)
        self.tree2 = Entity("assets/tree2.png", 450, 250, self.all_sprites_group)
        self.tree3 = Entity("assets/tree1.png", 1060, 250, self.all_sprites_group)
        
        self.plat1 = Entity("assets/plat1.png", 50, 550, self.all_sprites_group, self.all_plattform_group)
        self.plat2 = Entity("assets/plat3.png", 430, 550, self.all_sprites_group, self.all_plattform_group)
        self.plat3 = Entity("assets/plat2.png", 1080, 550, self.all_sprites_group, self.all_plattform_group)
        
        self.cristal1 = Entity("assets/crystal.png", 520, 400, self.all_sprites_group, self.cristal_group)
        self.cristal2 = Entity("assets/crystal.png", 870, 400, self.all_sprites_group, self.cristal_group)
        self.cristal3 = Entity("assets/crystal.png", 1150, 400, self.all_sprites_group, self.cristal_group)
        
        self.enemy1 = Enemy("assets/enemy0.png", 520, 502, self.all_sprites_group, self.enemy_group)
        self.enemy2 = Enemy("assets/enemy0.png", 800, 502, self.all_sprites_group, self.enemy_group)
        self.enemy3 = Enemy("assets/enemy0.png", 1100, 502, self.all_sprites_group, self.enemy_group)
        
        self.player = Hero("assets/idle0.png", 100, 450, self.all_sprites_group)
        
        self.hud = Entity("assets/hud.png", 50, 50, self.all_sprites_group)
        
    def draw(self, window):
        self.all_sprites_group.draw(window)
        
    def update(self):
        self.all_sprites_group.update()
        self.player.collisions(group=self.all_plattform_group, name="platform")
        self.player.collisions(group=self.cristal_group, kill=True, name="crystal")
        self.player.collisions(group=self.enemy_group, kill=False, name="enemy")
        self.HUD()
        
    def HUD(self):
        if self.player.crystals == 1:
            crystal = Entity("assets/icon_crystal.png", 136, 126, self.all_sprites_group)
        elif self.player.crystals == 2:
            crystal = Entity("assets/icon_crystal.png", 160, 126, self.all_sprites_group)
        elif self.player.crystals == 3:
            crystal = Entity("assets/icon_crystal.png", 185, 126, self.all_sprites_group)
            
        if self.player.lifes == 3:
            life1 = Entity("assets/icon_head.png", 140, 81, self.all_sprites_group)
            life2 = Entity("assets/icon_head.png", 177, 81, self.all_sprites_group)
            life3 = Entity("assets/icon_head.png", 214, 81, self.all_sprites_group)
        elif self.player.lifes == 2:
            life1 = Entity("assets/icon_head.png", 140, 81, self.all_sprites_group)
            life2 = Entity("assets/icon_head.png", 177, 81, self.all_sprites_group)
            life3 = Entity("assets/icon_dead.png", 214, 81, self.all_sprites_group)
        elif self.player.lifes == 1:
            life1 = Entity("assets/icon_head.png", 140, 81, self.all_sprites_group)
            life2 = Entity("assets/icon_dead.png", 177, 81, self.all_sprites_group)
            life3 = Entity("assets/icon_dead.png", 214, 81, self.all_sprites_group)
        else:
            life1 = Entity("assets/icon_dead.png", 140, 81, self.all_sprites_group)
            life2 = Entity("assets/icon_dead.png", 177, 81, self.all_sprites_group)
            life3 = Entity("assets/icon_dead.png", 214, 81, self.all_sprites_group)
            print("Game Over")