import pygame

class Ship:
    """class to manage ship"""
    def __int__(self, ai_game):
        """initialtize ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # load ship image and get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start ship bottom center
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)