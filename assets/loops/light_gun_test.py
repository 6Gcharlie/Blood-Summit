"""
This file contains code for a game loop with which the light gun can be tested.
If working correctly the screen will be populated by red squares which disappear
after being clicked!
"""

# - Module imports
import pygame
from assets import Enemy, Player

def test_loop(game):
    "A test environment to try out new code"

    # - Start using delta time here
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    game.get_prev_time()
    enemy = Enemy(game)
    player = Player()
    sky_colour = [255, 100, 127]
    floor_colour = [255, 54, 89]
    half_height = game.height / 2
    running = False

    shoot_to_start = font.render("Shoot to start", True, [255, 255, 255])

    # - This is the game loop
    while game.loop == "test environment":
        game.delta_clock()

        # - Events
        for event in pygame.event.get():
            if event.type == 1025 and event.button == 1:
                running = True

            game.events(event)
            player.events(event)
            enemy.events(event, player)

        # - Logic
        if running:
            enemy.update(game)
            player.update(game, enemy)

        ammo = font.render("Ammo: " + str(player.rounds), True, [0, 0, 0])

        # - Draw
        game.surface.fill(sky_colour)
        pygame.draw.rect(game.surface, floor_colour, [0, half_height, game.width, half_height])
        pygame.draw.rect(game.surface, [255, 255, 255], [0, half_height + 100, game.width / 4, 50])
        enemy.draw(game.surface)
        if running:
            game.surface.blit(ammo, [10, 10])
        else:
            game.surface.blit(shoot_to_start, [10, 10])
        game.draw()
