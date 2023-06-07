"""
Grunt.py contains details of the grunt enemy.
"""

import random
import pygame

# TODO: ADD ADDITIONAL ATTRIBUTES
#       - Is the enemy flying?
#       - Is the enemy ground borne?
#       - Can the enemy take flight and land?
#       - Can the enemy dodge? Does it have a dodge limit? Dodge response time? Dodge delay time?
#       - How angry is the enemy? Does this increase HP? Dodge? Dodge response time? Speed? Behavior? Damage?
#       - HP
#       - Shield/Armour variable? Is armour localised to a body part? How many hits does the armour take?
#       - Respawn/reposition without dying variable? How many times can it do that?

# TODO: MAKE THE GRUNT MOVE MORE TOWARD THE CENTRE OF THE SCREEN

class Grunt(pygame.sprite.Sprite):
    "The grunt is an enemy that deals melee damage to the enemy by reaching them"
    def __init__(self, game):
        self.width = 50
        self.height = 50
        self.set_surface()

        self.dead = False
        self.lives = 2
        self.flying = True
        self.running = True
        self.jog_speed = 0
        self.run_speed = 120

        self.speed = self.run_speed if self.running else self.jog_speed

        self.half_screen_width = game.width / 2
        self.half_screen_height = game.height / 2

        self.x_coord = random.randint(0, self.half_screen_width * 2)
        self.y_coord = random.randint(0, self.half_screen_height * 2)
        self.z_coord = 50

    def events(self, event):
        "temnp"
        # - pygame.MOUSEBUTTONDOWN is event number 1025
        if event.type == 1025:
            click_x, click_y = event.pos

            bullet_x = self.x_coord <= click_x <= self.x_coord + self.width
            bullet_y = self.y_coord <= click_y <= self.y_coord + self.height

            if bullet_x and bullet_y:
                if self.lives > 0:
                    self.respawn()
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

            self.set_surface()

    def draw(self, surface):
        "Draw the grunt onto the screen using the built in attributes"
        surface.blit(self.image, [self.x_coord, self.y_coord])

    def set_surface(self):
        "Set the size of the grunt surface"
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill([255, 0, 0])

    def respawn(self):
        "Allows the grunt to respawn on the screen"
        self.width = self.z_coord
        self.height = self.z_coord
        self.x_coord = random.randint(0, (self.half_screen_width * 2) - self.width)
        self.y_coord = random.randint(0, (self.half_screen_height * 2) - self.height)
        self.speed = self.run_speed if self.running else self.jog_speed
