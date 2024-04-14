from pygame import *

class GameSprite(sprite.Sprite):
    def __init__ (self, img, x, y, width, height, speed, window, speed_x = 0, speed_y = 0):
        super().__init__()
        self.img = transform.scale(image.load(img), (width, height))
        self.speed = speed
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.window = window
    
    def reset(self):
        self.window.blit(self.img, (self.rect.x, self.rect.y))