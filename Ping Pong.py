from pygame import *

# music
# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()

#create game window
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load("Water-color-BG.jpeg"), (700, 500))

# Game Sprite
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (width, height))
        self.speed = 2
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.way_ball = randint(1, 4)
    def blit_image(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        pass

class Paddel_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Paddel_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

# class Bot(GameSprite):
#     def update(self):
#         pass

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

ball = Ball("Ping-Pong-Ball.png", 330, 230, 40, 40, 5)

paddel_2 = Paddel_2("Black line.png", 20, 20, 25, 90, 6)
paddel_1 = Paddel_1("Black line.png", 600, 400, 25, 90, 6)
clock = time.Clock()
game = True

speed_x = 3
speed_y = 3
finish = False

while game:
    keys = key.get_pressed()
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:

        window.blit(background, (0, 0))

        paddel_1.update()
        paddel_2.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        # paddle collision
        if sprite.collide_rect(paddel_1, ball) or sprite.collide_rect(paddel_2, ball):
            speed_x *= -1
            speed_y *= 1

        # top/bottom of screen 
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        # player 1 lost
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200) )
            game_over = True

        # player 2 lost
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        paddel_1.blit_image()
        paddel_2.blit_image()
        ball.blit_image()
    
        ball.update()

    display.update()