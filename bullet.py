import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from ship"""

    def __init__(self, settings, screen, ship):
        super().__init__()
        self.screen = screen

        # Create bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, settings.bullet_width,
                                settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store bullet's position as decimal value
        self.y = float(self.rect.y)

        self.colour = settings.bullet_colour
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """Move bullet up screen"""
        # Update decimal position of bullet
        self.y -= self.speed_factor
        # Update rect position
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.colour, self.rect)
