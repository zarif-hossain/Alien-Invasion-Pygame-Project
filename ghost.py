import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    """A class to represent a ghost in the game."""
    
    def __init__(self, ai_game):
        """Initialize the ghost and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the ghost image and get its rect.
        self.image = pygame.image.load(self.settings.ghost_image)
        # Scale the ghost image to fit the screen dimensions
        self.image = pygame.transform.scale(self.image, 
            (self.settings.screen_width // 32, self.settings.screen_height // 16))
        self.rect = self.image.get_rect()

        # Start a new ghost at the top center of the screen
        self.rect.midtop = self.screen.get_rect().midtop

        # Store the ghost's exact position
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
