"""
This file contains code for a game loop with which the light gun can be tested.
If working correctly the screen will be populated by red squares which disappear
after being clicked!
"""

# - Module imports
import pygame
from assets import Enemy

def test_loop(game):
    "A test environment to try out new code"

    # - Start using delta time here
    game.get_prev_time()
    enemy = Enemy(game)
    sky_colour = [255, 100, 127]
    floor_colour = [255, 54, 89]
    half_height = game.height / 2

    # - This is the game loop
    while game.loop == "test environment":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            game.events(event)
            enemy.events(event)

        # - Logic
        enemy.update(game)

        # - Draw
        game.surface.fill(sky_colour)
        pygame.draw.rect(game.surface, floor_colour, [0, half_height, game.width, half_height])
        enemy.draw(game.surface)
        game.draw()
