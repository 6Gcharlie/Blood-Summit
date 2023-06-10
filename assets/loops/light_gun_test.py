"""
This file contains code for a game loop with which the light gun can be tested.
If working correctly the screen will be populated by red squares which disappear
after being clicked!
"""

import pygame
from assets import Enemy

def test_loop(game):
    "The test loop itself"
    game.get_prev_time()
    enemy = Enemy(game)
    shooting = False
    timer = 0

    # - Create test foreground:
    foreground = pygame.Surface([game.width, game.height / 2])
    foreground.fill([80, 80, 80])
    pygame.draw.line(foreground, [60, 60, 60], [0, 0], [game.width, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 6], [game.width, 6], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 12], [game.width, 12], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 18], [game.width, 18], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 24], [game.width, 24], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 36], [game.width, 36], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 48], [game.width, 48], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 96], [game.width, 96], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 192], [game.width, 192], 2)

    pygame.draw.line(foreground, [60, 60, 60], [0, 96], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 192], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 288], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [0, 480], [game.width / 2, 0], 2)

    pygame.draw.line(foreground, [60, 60, 60], [256, 480], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [512, 480], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [768, 480], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [1024, 480], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [game.width, 480], [game.width / 2, 0], 2)

    pygame.draw.line(foreground, [60, 60, 60], [game.width, 96], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [game.width, 192], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [game.width, 288], [game.width / 2, 0], 2)
    pygame.draw.line(foreground, [60, 60, 60], [game.width, 480], [game.width / 2, 0], 2)

    while game.loop == "test loop":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            if event.type == 1025:
                shooting = True

            game.events(event)
            enemy.events(event)

        # - Logic
        enemy.update(game)
        if shooting:
            if timer >= 10:
                shooting = False
                timer = 0

            timer += 100 * game.delta_time

        # - Draw
        game.surface.fill([100, 100, 100])
        pygame.draw.rect(
            game.surface, [80, 80, 80], [0, game.height / 2, game.width, game.height / 2]
        )
        game.surface.blit(foreground, [0, game.height / 2])
        enemy.draw(game.surface)

        if shooting:
            game.surface.fill([155, 155, 155])

        game.draw()
