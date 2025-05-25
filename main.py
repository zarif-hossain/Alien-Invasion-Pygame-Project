import sys
import pygame

from ship import Ship
from bullet import Bullet
from ghost import Ghost
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # Create a screen object and set it to fullscreen mode.
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 

        # Name game window.
        pygame.display.set_caption("FANTASMA")

        # Initialize settings.
        self.settings = Settings()
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.settings.ship_speed_factor = self.settings.screen_width / 480
        
        # Make an instance of Ship after the screen has been created
        # and self argument refers to the current instance of AlienInvasion
        # to give Ship object access to the game's resources
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.ghost = pygame.sprite.Group()
        self._create_fantasma()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            # Check for QUIT event.
            if event.type == pygame.QUIT:
                sys.exit()
            # Check for KEYDOWN events.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # Check for KEYUP events.
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            # Quit the game.
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # Move the ship up.
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down.
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            # Stop moving the ship to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop moving the ship to the left.
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            # Stop moving the ship up.
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Stop moving the ship down.
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and remove old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Remove bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fantasma(self):
        """Create a ghost and place it at the top center of the screen."""
        # Create a new ghost and add it to the ghost group.
        new_ghost = Ghost(self)
        self.ghost.add(new_ghost)
    
    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ghost.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()