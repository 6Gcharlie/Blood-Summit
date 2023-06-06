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

    while game.loop == "test loop":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            game.events(event)
            grunt.events(event)

        # - Logic
        grunt.update(game)

        # - Draw
        game.surface.fill([100, 100, 100])
        grunt.draw(game.surface)
        game.draw()
