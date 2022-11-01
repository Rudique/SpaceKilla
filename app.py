import pygame
from sprites import Player, Mob
from settings import BLACK, GREEN, screen, FPS, all_sprites, mobs, bullets, \
    background, background_rect, WHITE, WIDTH, expl_sounds
import random
from utils import draw_text, draw_shield_bar, newmob

if __name__ == "__main__":
    # создаем игру и окно
    pygame.init()
    pygame.mixer.init()  # для звука

    pygame.display.set_caption("SpaceKilla")
    clock = pygame.time.Clock()

    player = Player()
    all_sprites.add(player)

    for i in range(10):
        newmob()

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
            newmob()

        # Проверка, не ударил ли моб игрока
        hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius / 2
            if player.shield <= 0:
                running = False

        screen.fill(BLACK)
        screen.blit(background, background_rect)

        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()
