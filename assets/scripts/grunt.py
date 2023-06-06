"""
Grunt.py contains details of the grunt enemy.
"""

import random
import pygame

# TODO: REFACTOR THE CODE SO THAT "self.speed" IS USED INSTEAD OF OTHER SET SPEEDS
#       - This will significantly reduce calculation time
#       - And will also allow for the speed to be affected and reset easily

# TODO: CREATE A FUNCTION FOR RESETTING/RESPAWNING THE ENEMY
#       - Maybe add an attribute which dictates whether it can respawn?

# TODO: ADD ADDITIONAL ATTRIBUTES
#       - Is the enemy flying?
#       - Is the enemy ground borne?
#       - Can the enemy take flight and land?
#       - Can the enemy dodge? Does it have a dodge limit? Dodge response time? Dodge delay time?
#       - How angry is the enemy? Does this increase HP? Dodge? Dodge response time? Speed? Behavior? Damage?
#       - HP
#       - Shield/Armour variable? Is armour localised to a body part? How many hits does the armour take?
#       - Respawn/reposition without dying variable? How many times can it do that?

# TODO: FIX MAKING THE GRUNT MOVE FASTER THE BIGGER IT IS
#       - Try using "z_coord" to track when is a good time to increase the speed?

# TODO: MAKE THE GRUNT MOVE MORE TOWARD THE CENTRE OF THE SCREEN

class Grunt(pygame.sprite.Sprite):
    "The grunt jogs at the player and kills them once they reach them"
    def __init__(self, game):
        self.width = 50
        self.height = 50
        self.set_surface()

        self.flying = True
        self.movement = "walking"
        self.walk_speed = 20
        self.jog_speed = 40
        self.run_speed = 80
        self.speed = 0

        self.half_screen_width = game.width / 2
        self.half_screen_height = game.height / 2

        self.x_coord = random.randint(0, self.half_screen_width * 2)
        self.y_coord = random.randint(0, self.half_screen_height * 2)
        self.z_coord = 0

    def events(self, event):
        "temnp"
        # - pygame.MOUSEBUTTONDOWN is event number 1025
        if event.type == 1025:
            click_x, click_y = event.pos

            bullet_x = self.x_coord <= click_x <= self.x_coord + self.width
            bullet_y = self.y_coord <= click_y <= self.y_coord + self.height

            if bullet_x and bullet_y:
                self.width = 50
                self.height = 50

                screen_width = self.half_screen_width * 2
                screen_height = self.half_screen_height * 2

                self.x_coord = random.randint(0, screen_width - self.width)
                self.y_coord = random.randint(0, screen_height - self.height)
                self.walk_speed = 20
                self.jog_speed = 40
                self.run_speed = 80
                self.z_coord = 0
                print("clicked")

    def update(self, game):
        "update script for the enemy"
        # - Have the grunt move toward the screen width centre
        if self.x_coord <= self.half_screen_width - self.width / 2:
            match self.movement:
                case "walking":
                    self.x_coord += self.walk_speed * game.delta_time
                case "jogging":
                    self.x_coord += self.jog_speed * game.delta_time
                case "running":
                    self.x_coord += self.run_speed * game.delta_time

        if self.x_coord >= self.half_screen_width - self.width / 2:
            match self.movement:
                case "walking":
                    self.x_coord -= self.walk_speed * 2 * game.delta_time
                case "jogging":
                    self.x_coord -= self.jog_speed * 2 * game.delta_time
                case "running":
                    self.x_coord -= self.run_speed * 2 * game.delta_time

        if self.y_coord <= self.half_screen_height - self.height / 2:
            match self.movement:
                case "walking":
                    self.y_coord += self.walk_speed * game.delta_time
                case "jogging":
                    self.y_coord += self.jog_speed * game.delta_time
                case "running":
                    self.y_coord += self.run_speed * game.delta_time

        if self.y_coord >= self.half_screen_height - self.height / 2:
            match self.movement:
                case "walking":
                    self.y_coord -= self.walk_speed * 2 * game.delta_time
                case "jogging":
                    self.y_coord -= self.jog_speed * 2 * game.delta_time
                case "running":
                    self.y_coord -= self.run_speed * 2 * game.delta_time

        # - Have the grunt increase in size to give the illusion of getting closer
        if self.height < game.height:
            match self.movement:
                case "walking":
                    self.height += self.walk_speed * game.delta_time
                case "jogging":
                    self.height += self.jog_speed * game.delta_time
                case "running":
                    self.height += self.run_speed * game.delta_time

        if self.width < game.height:
            match self.movement:
                case "walking":
                    self.width += self.walk_speed * game.delta_time
                case "jogging":
                    self.width += self.jog_speed * game.delta_time
                case "running":
                    self.width += self.run_speed * game.delta_time

        match self.movement:
            case "walking":
                self.walk_speed += 1
            case "jogging":
                self.jog_speed += 1
            case "running":
                self.run_speed += 1

        self.set_surface()

    def set_surface(self):
        "Set the size of the grunt surface"
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill([255, 0, 0])

    def draw(self, surface):
        "Draw the grunt onto the screen using the built in attributes"
        surface.blit(self.image, [self.x_coord, self.y_coord])
