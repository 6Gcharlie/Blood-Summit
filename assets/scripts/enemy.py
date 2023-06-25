"""
enemy.py contains details of the Enemy class.
"""

import os
import random
import pygame

###################################################################################################
## The Enemy class is used to construct all enemies in this game from basic to complex, it takes ##
## a wide range of attributes with which the computer can dynamically control the enemies        ##
## behaviour!                                                                                    ##
###################################################################################################
class Enemy(pygame.sprite.Sprite):
    "The Enemy is an enemy that deals melee damage to the enemy by reaching them"
    # The __init__ constructor creates the initial variables for the class
    # object        game        The game parameter stores all attributes about the game
    def __init__(self, game):
        "Construct the class with the attributes given"
        # - Basic attributes for the enemy
        self.hitpoints = 100
        self.flying = False
        self.lives = 99
        self.jog_speed = 0
        self.run_speed = 120
        self.dead = False
        self.angry = False
        self.running = False
        self.damaging = False

        # - Can the enemy dodge? If so, how far, how fast, how many times?
        self.dodges = False
        self.dodge_count = 0
        self.dodge_reaction_time = 0
        self.dodge_distance = 0
        self.dodge_end_lag = 0

        # - Does the enemy have armour? If so, where, how much, how much damage to damage it?
        self.armoured = False
        self.armour = {
            "head": {"armoured": False, "hitpoints": 0, "threshold": 0},
            "body": {"armoured": False, "hitpoints": 0, "threshold": 0}
        }

        # - Every enemy has hitboxes, where are they and how big are they?
        self.hitboxes = {
            "head": {"x": 0, "y": 0, "width": 50, "height": 50},
            "body": {"x": 0, "y": 50, "width": 50, "height": 50}
        }

        # - Set the image of the enemy
        self.url = "assets/sprites/mystery_figure.png"
        self.image = pygame.image.load(os.path.join(self.url)).convert_alpha()

        # - Save the screen center
        self.half_screen_width = game.width / 2
        self.half_screen_height = game.height / 2

        # - Lets draw our enemy to the screen & spawn them
        self.reset_size()
        self.image = pygame.transform.scale(self.image, [self.width, self.height])
        self.set_surface()
        self.spawn()



    # The events method captures and manages all event for the enemy
    # object        event           The event object stores all event related information
    def events(self, event, player):
        "All enemy events are captured and managed in this method"
        # - pygame.MOUSEBUTTONDOWN is event number 1025
        if event.type == 1025 and player.rounds > 0 and event.button == 1:
            click_x, click_y = event.pos # - Get the position of the click

            # - Now let's work out of the bullet hit us
            bullet_x = self.x_coord <= click_x <= self.x_coord + self.width
            bullet_y = self.y_coord <= click_y <= self.y_coord + self.height

            # - If the bullet hit, die or respawn
            if bullet_x and bullet_y:
                if self.lives > 1:
                    self.reset_size()
                    self.spawn()
                    self.lives -= 1
                else:
                    self.dead = True



    # The update method is for processing logic for the enemy that doesn't require an event trigger
    # object        game            The game object stores information related to the game/window
    def update(self, game):
        "Update the enemy based on the data provided"
        # - Have the Enemy move toward the centre of the screen, if smaller than the screen & alive
        if not self.dead:
            if self.height < game.height and self.width < game.width:
                # - Let's make the enemy move faster based on width
                self.speed += (self.width / 4) * game.delta_time

                # - If we're not in the centre of the screen, move toward it
                if self.x_coord <= self.half_screen_width - self.width / 2:
                    self.x_coord += self.speed * game.delta_time
                if self.x_coord >= self.half_screen_width - self.width / 2:
                    self.x_coord -= (self.speed * 2) * game.delta_time
                if self.y_coord <= self.half_screen_height - self.height / 2:
                    self.y_coord += self.speed * game.delta_time
                if self.y_coord >= self.half_screen_height - self.height / 2:
                    self.y_coord -= self.speed * game.delta_time

                # - Have the Enemy increase in size until it fits the screen
            if self.y_coord + self.height < (game.height / 2) + 100 or self.x_coord > game.width / 4:
                if self.height < game.height:
                    self.height += (self.speed * 2) * game.delta_time
                else:
                    self.damaging = True

                if self.width < game.height / 2:
                    self.width += self.speed * game.delta_time
                else:
                    self.damaging = True

            # - Resize the image to fit the bigger surface
            self.image = pygame.image.load(os.path.join(self.url)).convert_alpha()
            self.image = pygame.transform.scale(self.image, [self.width, self.height])
            self.set_surface()



    # The draw method contains little code but simplifies the process of drawing the enemy
    # object        surface         The surface we're going to draw the enemy onto
    def draw(self, surface):
        "Draw the Enemy onto the screen using the built in attributes"
        pygame.draw.rect(self.surface, [255, 255, 255], [0, self.height - 5, 5, 5])
        surface.blit(self.surface, [self.x_coord, self.y_coord])



    # This method is used to set the width and the height of the surface
    def reset_size(self):
        "temp"
        self.z_coord = random.randint(60, 100)
        self.width = self.z_coord / 2
        self.height = self.z_coord



    #
    #
    #
    def set_surface(self):
        "Set the size of the Enemy surface"
        self.surface = pygame.Surface([self.width, self.height], 65536, 32)
        self.surface = self.surface.convert_alpha()
        self.surface.blit(self.image, [0, 0, self.width, self.height])



    #
    #
    #
    def spawn(self):
        "Allows the Enemy to respawn on the screen"
        self.speed = self.run_speed if self.running else self.jog_speed

        if self.flying:
            self.x_coord = random.randint(0, (self.half_screen_width * 2) - self.width)
            self.y_coord = random.randint(0, self.half_screen_height - self.height)
        else:
            self.x_coord = random.randint(0, (self.half_screen_width * 2))
            self.y_coord = self.half_screen_height - (self.height / 2)
