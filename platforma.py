from gameSprite import GameSprite
from pygame import *

class Platform(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y + self.rect.height < 700:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y + self.rect.height < 700:
            self.rect.y += self.speed