"""
Grunt.py contains details of the grunt enemy.
"""

import pygame

class Grunt(pygame.sprite.Sprite):
    "The grunt jogs at the player and kills them once they reach them"
    def __init__(self, game):
        self.width = 50
        self.height = 50
        self.set_surface()

        self.movement = "running"
        self.walk_speed = 10
        self.jog_speed = 20
        self.run_speed = 40

        self.half_screen_width = game.width / 2
        self.half_screen_height = game.height / 2

        self.x_coord = 50
        self.y_coord = 300
        self.z_coord = 0

    def update(self, game):
        "update script for the enemy"

        # TODO: KEEP THE SQUARE CENTRAL UNTIL IT REACHES SCREEN HEIGHT

        # - Have the grunt move toward the screen width centre
        if self.x_coord < self.half_screen_width - self.width / 2:
            match self.movement:
                case "walking":
                    self.x_coord += self.walk_speed * game.delta_time
                case "jogging":
                    self.x_coord += self.jog_speed * game.delta_time
                case "running":
                    self.x_coord += self.run_speed * game.delta_time

        if self.y_coord < self.half_screen_height - self.height / 2:
            match self.movement:
                case "walking":
                    self.y_coord += self.walk_speed * game.delta_time
                case "jogging":
                    self.y_coord += self.jog_speed * game.delta_time
                case "running":
                    self.y_coord += self.run_speed * game.delta_time

        if self.x_coord > self.half_screen_width - self.width / 2:
            self.x_coord = self.half_screen_width - self.width / 2

        if self.y_coord > self.half_screen_height - self.height / 2:
            self.y_coord = self.half_screen_height - self.height / 2

        # - Have the grunt increase in size to give the illusion of getting closer
        if self.height < game.height:
            self.height += 20 * game.delta_time

        if self.width < game.height:
            self.width += 20 * game.delta_time

        self.set_surface()

    def set_surface(self):
        "Set the size of the grunt surface"
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill([255, 0, 0])

    def draw(self, surface):
        "Draw the grunt onto the screen using the built in attributes"
        surface.blit(self.image, [self.x_coord, self.y_coord])
