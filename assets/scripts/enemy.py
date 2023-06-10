"""
Enemy.py contains details of the Enemy enemy.
"""

import os
import random
import pygame

class Enemy(pygame.sprite.Sprite):
    "The Enemy is an enemy that deals melee damage to the enemy by reaching them"
    def __init__(self, game):
        # ENEMY TYPES:
        # - Autocrat
        self.type = "autocrat"
        self.set_enemy(1)

        self.dead = False
        self.angry = False
        self.running = False

        self.image = pygame.image.load(os.path.join("assets/sprites/mystery_figure.png")).convert_alpha()

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
                if self.lives > 1:
                    self.spawn()
                    self.lives -= 1
                else:
                    self.dead = True

    def update(self, game):
        "update script for the enemy"
        # - Have the Enemy move toward the centre of the screen, if it is smaller than the screen
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

            # - Have the Enemy increase in size until it fits the screen
            if self.height < game.height:
                self.height += self.speed * game.delta_time
            if self.width < game.height:
                self.width += self.speed * game.delta_time

            self.image = pygame.image.load(os.path.join("assets/sprites/mystery_figure.png")).convert_alpha()
            self.image = pygame.transform.scale(self.image, [self.width, self.height])
            self.set_surface()

    def draw(self, surface):
        "Draw the Enemy onto the screen using the built in attributes"
        surface.blit(self.surface, [self.x_coord, self.y_coord])

    def set_surface(self):
        "Set the size of the Enemy surface"
        self.surface = pygame.Surface([self.width, self.height], 65536, 32)
        self.surface = self.surface.convert_alpha()
        self.surface.blit(self.image, [0, 0, self.width, self.height])

    def spawn(self):
        "Allows the Enemy to respawn on the screen"
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

    def set_enemy(self, level):
        "Set enemy type"
        match self.type:
            case "autocrat":
                match level:
                    case 1:
                        self.hitpoints = 100
                        self.flying = False
                        self.lives = 10
                        self.jog_speed = 0
                        self.run_speed = 120

                        self.dodges = False
                        self.dodge_count = 0
                        self.dodge_reaction_time = 0
                        self.dodge_distance = 0
                        self.dodge_end_lag = 0

                        self.armoured = False
                        self.armour = {
                            "head": {"armoured": False, "hitpoints": 0, "threshold": 0},
                            "body": {"armoured": False, "hitpoints": 0, "threshold": 0}
                        }

                        self.hitboxes = [
                            {"box": "head", "x": 0, "y": 0, "width": 50, "height": 50},
                            {"box": "body", "x": 0, "y": 50, "width": 50, "height": 50}
                        ]
