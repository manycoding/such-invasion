import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to represent single alien in fleet"""

    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Load alien image and set its rect attribute
        self.image = pygame.image.load('images/coin.png')
        self.rect = self.image.get_rect()

        # Start each new alien near top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right."""
        self.x += self.settings.alien_speed_factor
        self.rect.x = self.x
