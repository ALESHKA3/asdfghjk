from pygame import *
from gameSprite import *
from platforma import *
from ball import *
from random import randint

ball_x = randint(-5, 5)
ball_y = randint(-5, 5)

while ball_x == 0:
    ball_speed_x = randint(-5, 5)

while ball_y == 0:
    ball_speed_y = randint(-5, 5)
    
BGCOLOR = (230, 200, 89)
TEXTCOLOR = (134, 74, 249)

SCREENSIZE = (700, 700)

window = display.set_mode(SCREENSIZE)
display.set_caption("ping-pong")

timer = time.Clock()

run = True

platform_left = Platform("platform.png", 10, 330, 20, 100, 5, window)
platform_right = Platform("platform.png", 670, 330, 20, 100, 5, window)

ball = Ball('ball.jpg', 337, 337, 50, 50, 0, window, 2, -2)

font.init()
textFont = font.Font(None, 100)

game_over = False

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if game_over == False:
        window.fill(BGCOLOR)

        platform_left.reset()
        platform_left.update_left()

        platform_right.reset()
        platform_right.update_right()

        ball.isCollide(platform_left)
        ball.isCollide(platform_right)

        ball.move()
        ball.reset()

        if ball.whoLose():
            if ball.whoLose() == 'left':
                loseText = textFont.render ('LEFT LOSE', True, (255, 0, 0))    
            else:
                loseText = textFont.render ('RIGHT LOSE', True, (255, 0, 0))
            window.blit(loseText, (150, 320))
            game_over = True

    display.update()
    timer.tick(60)