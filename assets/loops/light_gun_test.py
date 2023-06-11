"""
This file contains code for a game loop with which the light gun can be tested.
If working correctly the screen will be populated by red squares which disappear
after being clicked!
"""

# - Module imports
import pygame
from assets import Enemy

# - This is the game loop
def test_loop(game):
    "A test environment to try out new code"

    # - Start using delta time here
    game.get_prev_time()

    enemy = Enemy(game)
    foreground = create_foreground(game)

    while game.loop == "test environment":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            game.events(event)
            enemy.events(event)

        # - Logic
        enemy.update(game)

        # - Draw
        game.surface.fill([100, 100, 100])
        game.surface.blit(foreground, [0, game.height / 2])
        enemy.draw(game.surface)
        game.draw()


#
#
#
#
#
def create_foreground(game):
    "This function creates a test foreground to demonstrate depth perception"
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

    return foreground
