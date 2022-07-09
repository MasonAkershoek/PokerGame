import pygame
from settings import *


class PlayerUI(pygame.sprite.Sprite):
    def __init__(self, pos, text_size, path, game):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, text_size)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.game_type = game

    def update_p_cash(self, text):
        surf = self.font.render('Cash: ' + str(text), True, 'white')
        rect = surf.get_rect(center = (((self.display_surface.get_width() / 2) - 530), (self.display_surface.get_height() - 75)))
        self.display_surface.blit(surf,rect)

    def update_hand(self, hand):
        terms = ['Junk', 'Pair', '2 Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind', 'Straight Flush', 'Royal Flush']
        for x, term in enumerate(terms):
            if x == hand[0]:
                surf = self.font.render('Hand: ' + str(term), True, 'white')
                rect = surf.get_rect(center = (((self.display_surface.get_width() / 2) + 530), (self.display_surface.get_height() - 100)))
                self.display_surface.blit(surf,rect)

    def game(self):
        game_types = ['Five Card']
        for x, term in enumerate(game_types):
            if self.game_type == 'five_card':
                surf = self.font.render('Game: ' + str(term), True, 'white')
                rect = surf.get_rect(center = (((self.display_surface.get_width() / 2) + 530), (self.display_surface.get_height() - 50)))
                self.display_surface.blit(surf,rect)

    def update(self, text, hand):
        self.display_surface.blit(self.image, self.rect)
        self.update_p_cash(text)
        self.game()
        if len(hand) > 0:
            self.update_hand(hand)
    
class PotUI(pygame.sprite.Sprite):
    def __init__(self, pos, text_size, path):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, text_size)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.pos = pos

    def update_pot(self, pot):
        surf = self.font.render('Pot: ' + str(pot), True, 'white')
        rect = surf.get_rect(center = self.pos)
        self.display_surface.blit(surf,rect)
    
    def update(self, pot):
        self.display_surface.blit(self.image, self.rect)
        self.update_pot(pot)
