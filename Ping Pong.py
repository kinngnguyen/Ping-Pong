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
        self.way_ball = randint(1, 4)
    def blit_image(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        pass

class Paddel_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_UP] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

class Paddel_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_S] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_W] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

ball = Ball("Ping-Pong-Ball.png", 330, 230, 40, 40, 5)

paddel_1 = Paddel_1("Black Line", 20, 20, 75, 90, 5)
paddel_2 = Paddel_2("Black Line", 500, 400, 75, 90, 5)
clock = time.Clock()
game = True
while game:
    keys = key.get_pressed()
    clock.tick(60)
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background(0, 0))

    paddel_1.blit_image()
    paddel_2.blit_image()

    paddel_1.update()
    paddel_2.update()

    ball.update()



display.update()