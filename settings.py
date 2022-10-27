import pygame

from os import path

WIDTH = 480
HEIGHT = 640
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
pygame.mixer.init()


img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))

pygame.mixer.music.load(path.join(snd_dir, 'Battle.mp3'))
pygame.mixer.music.set_volume(0.4)

background = pygame.image.load(path.join(img_dir, 'last.jpg')).convert()
background = pygame.transform.scale(background, (480, 640))
background_rect = background.get_rect()

player_img = pygame.image.load(path.join(img_dir, "sneaky-toast-idle.gif")).convert()

bullet_img = pygame.image.load(path.join(img_dir, "burger.png")).convert()

meteor_list = ['fries.png', 'Microondas.png',
               'apple.png',   'ham.png', 'strawberry.png',
               'meteorBrown_med3.png', 'meteorGrey_big2.png']
meteor_images = []

for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

mob_img = pygame.image.load(path.join(img_dir, 'apple.png'))

