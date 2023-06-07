"""
Grunt.py contains details of the grunt enemy.
"""

import os
import random
import pygame

class Grunt(pygame.sprite.Sprite):
    "The grunt is an enemy that deals melee damage to the enemy by reaching them"
    def __init__(self, game):
        self.hitpoints = 100
        self.dead = False
        self.angry = False
        self.lives = 99
        self.flying = True
        self.running = True
        self.jog_speed = 0
        self.run_speed = 120

        self.dodges = False
        self.dodge_count = 0
        self.dodge_reaction_time = 10
        self.dodge_distance = 0
        self.dodge_end_lag = 10

        self.armour = {
            "head": {"armoured": False, "hitpoints": 100, "threshold": 40},
            "body": {"armoured": False, "hitpoints": 100, "threshold": 40}
        }

        self.peter = pygame.image.load(os.path.join("assets/sprites/mystery_figure.png")).convert_alpha()

        self.half_screen_width = game.width / 2
        self.half_screen_height = game.height / 2

        self.spawn()
        self.set_surface()

    def events(self, event):
        "temnp"
        # - pygame.MOUSEBUTTONDOWN is event number 1025
        if event.type == 1025:
            click_x, click_y = event.pos

            bullet_x = self.x_coord <= click_x <= self.x_coord + self.width
            bullet_y = self.y_coord <= click_y <= self.y_coord + self.height

            if bullet_x and bullet_y:
                if self.lives > 0:
                    self.spawn()
                    self.lives -= 1
                else:
                    self.dead = True

    def update(self, game):
        "update script for the enemy"
        # - Have the grunt move toward the centre of the screen, if it is smaller than the screen
        if not self.dead:
            if self.height < game.height and self.width < game.width:
                self.speed += (self.width / 2) * game.delta_time

                if self.x_coord <= self.half_screen_width - self.width / 2:
                    self.x_coord += self.speed * game.delta_time
                if self.x_coord >= self.half_screen_width - self.width / 2:
                    self.x_coord -= (self.speed * 2) * game.delta_time
                if self.y_coord <= self.half_screen_height - self.height / 2:
                    self.y_coord += self.speed * game.delta_time
                if self.y_coord >= self.half_screen_height - self.height / 2:
                    self.y_coord -= (self.speed * 2) * game.delta_time

            # - Have the grunt increase in size until it fits the screen
            if self.height < game.height:
                self.height += self.speed * game.delta_time
            if self.width < game.height:
                self.width += self.speed * game.delta_time

            self.peter = pygame.image.load(os.path.join("assets/sprites/mystery_figure.png")).convert_alpha()
            self.peter = pygame.transform.scale(self.peter, [self.width, self.height])
            self.set_surface()

    def draw(self, surface):
        "Draw the grunt onto the screen using the built in attributes"
        surface.blit(self.image, [self.x_coord, self.y_coord])

    def set_surface(self):
        "Set the size of the grunt surface"
        self.image = pygame.Surface([self.width, self.height], 65536, 32)
        self.image = self.image.convert_alpha()
        self.image.blit(self.peter, [0, 0, self.width, self.height])

    def spawn(self):
        "Allows the grunt to respawn on the screen"
        self.z_coord = random.randint(10, 100)
        self.width = self.z_coord
        self.height = self.z_coord
        self.speed = self.run_speed if self.running else self.jog_speed

        if self.flying:
            self.x_coord = random.randint(0, (self.half_screen_width * 2) - self.width)
            self.y_coord = random.randint(0, self.half_screen_height - self.height)
        else:
            self.x_coord = random.randint(0, (self.half_screen_width * 2) - self.width)
            self.y_coord = self.half_screen_height - (self.height / 2)
