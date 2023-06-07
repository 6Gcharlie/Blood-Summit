"""
This file contains code for a game loop with which the light gun can be tested.
If working correctly the screen will be populated by red squares which disappear
after being clicked!
"""

import pygame
from assets import Grunt

def test_loop(game):
    "The test loop itself"
    game.get_prev_time()
    grunt = Grunt(game)
    shooting = False
    timer = 0

    while game.loop == "test loop":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            if event.type == 1025:
                shooting = True

            game.events(event)
            grunt.events(event)

        # - Logic
        grunt.update(game)
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
        
        grunt.draw(game.surface)

        if shooting:
            game.surface.fill([155, 155, 155])

        game.draw()
