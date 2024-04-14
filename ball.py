from gameSprite import GameSprite
from pygame import*

class Ball(GameSprite):
    def move(self):
        if self.rect.y < 0 or self.rect.y > 700 - self.rect.height:
            self.speed_y *= -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def isCollide (self, platform):


        if self.rect.colliderect(platform):
            self.speed_x *= -1

    def whoLose (self):
        if self.rect.x < 0:
            return 'left'
        if self.rect.x > 700 - self.rect.width:
            return 'right'