import pygame
from sprites import Player, Mob
from settings import BLACK, screen, FPS, all_sprites, mobs, bullets, \
    background, background_rect, WHITE, WIDTH, expl_sounds
import random


# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука

pygame.display.set_caption("SpaceKilla")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


player = Player()
all_sprites.add(player)

for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

score = 0
pygame.mixer.music.play(loops=-1)
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        random.choice(expl_sounds).play()
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    # Проверка, не ударил ли моб игрока
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
    if hits:
        running = False

    screen.fill(BLACK)
    screen.blit(background, background_rect)

    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
