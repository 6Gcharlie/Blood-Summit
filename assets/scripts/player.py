"""
player.py creates the wizard the player uses throughout the game.
"""

import os
import pygame

pygame.mixer.init()

class Player(pygame.sprite.Sprite):
    "Player class temporary placeholder"
    def __init__(self):
        "Constructs the class with attributes"
        self.weapon = "pistol"
        self.lives = 3
        self.hitpoints = 100
        self.gunshot = pygame.mixer.Sound(os.path.join("assets/sounds/gunshot.mp3"))
        self.trigger = pygame.mixer.Sound(os.path.join("assets/sounds/trigger.mp3"))
        self.reload = pygame.mixer.Sound(os.path.join("assets/sounds/reload.mp3"))
        self.rounds = 17



    #
    #
    #
    def events(self, event):
        "All player events are captured and managed in this method"
        # - Gun is shot
        if event.type == 1025:
            if event.button == 1:
                match self.weapon:
                    case "pistol":
                        if self.rounds > 0:
                            self.gunshot.play()
                            self.rounds -= 1
                        else:
                            self.trigger.play()
            elif event.button == 3:
                match self.weapon:
                    case "pistol":
                        self.rounds = 17
                        self.reload.play()



    #
    #
    #
    def update(self, game, enemy):
        "Temporary placeholder"
        if enemy.damaging:
            self.hitpoints -= 100 * game.delta_time