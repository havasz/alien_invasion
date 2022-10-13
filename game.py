import sys
import pygame

class AlienInvasion:
    """overall class to manage assets and behavior"""

    def __int__(self):
        """initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start main loop"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen during each pass through loop
            self.screen.fill(self.bg_color)

                    # make most recently drawn screen visable
                    pygame.display.flip()
if __name__ == '__main__':
    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()

class Settings:
    """class to store all settings"""

    def __int__(self):
        """initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)