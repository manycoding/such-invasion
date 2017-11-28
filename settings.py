class Settings():
    """A class to store game settings"""

    def __init__(self):
        # display
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Alien settings
        self.alien_speed_factor = 1

        # bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3
