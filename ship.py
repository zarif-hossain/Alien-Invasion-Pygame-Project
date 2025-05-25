import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship3.png')
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        # Start a new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.screen_rect.height - (self.settings.ship_height * 2)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed_factor

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)