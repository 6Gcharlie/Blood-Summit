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
    total_enemies = 20

    border_size = 20

    # - Text prompts defined before game start
    shoot_to_start = font.render("Shoot to start", True, [255, 255, 255])
    game_over = font.render("GAME OVER", True, [255, 0, 0])

    # - This is the game loop
    while game.loop == "test environment":
        game.delta_clock()

        # - Initial checks
        if enemy.dead:
            player.score += enemy.points
            if total_enemies > 0:
                enemy = Enemy(game)
            else:
                game.state = "post-game"

            total_enemies -= 1



        # - Events
        for event in pygame.event.get():
            if event.type == 1025 and event.button == 1 and game.state == "pre-game":
                game.state = "play"
            else:
                game.events(event)
                enemy.events(event, player)
                player.events(game,event)



        # - Logic
        if game.state == "play":
            enemy.update(game)
            player.update(game, enemy)
            game.update_timer()

            ammo = font.render("Ammo: " + str(player.rounds), True, [0, 0, 0])
            score_graphic = font.render("Score: " + str(player.score), True, [0, 0, 0])
            timer_graphic = font.render("Time: " + str(game.timer), True, [0, 0, 0])



        # - Draw
        game.surface.fill(sky_colour)
        pygame.draw.rect(game.surface, floor_colour, [0, half_height, game.width, half_height])
        enemy.draw(game.surface)

        if game.state == "pre-game":
            game.surface.blit(shoot_to_start, [border_size + 10, border_size + 10])
        elif game.state == "play":
            game.surface.blit(timer_graphic, [border_size + 10, border_size + 10])
            game.surface.blit(ammo, [border_size + 10, border_size + 30])
            game.surface.blit(score_graphic, [border_size + 10, border_size + 50])
        else:
            game.surface.blit(game_over, [border_size + 10, border_size + 10])

        pygame.draw.rect(game.surface, [255, 255, 255], [0, 0, game.width, border_size])
        pygame.draw.rect(game.surface, [255, 255, 255], [0, 0, border_size, game.height])
        pygame.draw.rect(game.surface, [255, 255, 255], [0, game.height - border_size, game.width, border_size])
        pygame.draw.rect(game.surface, [255, 255, 255], [game.width - border_size, 0, border_size, game.height])

        game.draw()
