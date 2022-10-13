import sys
import pygame

class AlienInvasion:
    """overall class to manage assets and behavior"""

    def __int__(self):
        """initialize the game and create game resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """start main loop"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                    # make most recently drawn screen visable
                    pygame.display.flip()
if __name__ == '__main__':
    # make a game instance and run game
    ai = AlienInvasion()
    ai.run_game()