class Settings:
    """Stores all settings for the Alien Invasion game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (0, 0, 20)

        # Ship settings
        self.ship_speed_factor = 20

        # Bullet settings
        self.bullet_speed_factor = 25
        self.bullet_width = 7
        self.bullet_height = 22
        self.bullet_color = (0, 0, 255)

        # Alien settings
        self.alien_speed_factor = 1.0