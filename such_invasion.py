import game_functions as gf
import pygame
from pygame.sprite import Group
import settings
from ship import Ship


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    game_settings = settings.Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,
                                      game_settings.screen_height))
    pygame.display.set_caption("SUCH SHOOTING MANY LAUGH")

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(game_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # Clear bullets
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(game_settings, screen, ship, aliens, bullets)

        pygame.display.flip()


run_game()
