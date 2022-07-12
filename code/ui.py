import pygame
from settings import *
from random import randint
import game_data


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
        terms = [('High Card: ' + str(hand[1])), 'Pair', '2 Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind', 'Straight Flush', 'Royal Flush']
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


class OpponentUI(pygame.sprite.Sprite):
    def __init__(self, pos, text_size, path):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, text_size)
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)

        print(self.rect.centerx)
        self.faces = self.get_faces()
        self.face = self.faces[0]
        self.face_rect = self.face.get_rect(center = (self.rect.centerx ,150))

        self.title = self.font.render('Opponent', True, 'white')
        self.title_rect = self.title.get_rect(center = (self.rect.centerx, 95))

    def get_faces(self):
        paths = ['../graphics/opponent/idle.png', '../graphics/opponent/lose.png', '../graphics/opponent/think.png', '../graphics/opponent/win1.png', '../graphics/opponent/win2.png']
        faces = []
        for x in paths:
            faces.append(pygame.image.load(x).convert_alpha())
        return faces

    def change_face(self, face):
        if face == 'idle':
            self.face = self.faces[0]
        elif face == 'think':
            self.face = self.faces[2]
        elif face == 'lose':
            self.face = self.faces[1]
        elif face == 'win':
            c = randint(1,2)
            if self.face != self.faces[3] and self.face != self.faces[4]:
                if c == 1:
                    self.face = self.faces[3]
                else:
                    self.face = self.faces[4]

    def update_p_cash(self, text):
        surf = self.font.render('Cash: ' + str(text), True, 'white')
        rect = surf.get_rect(center = (self.rect.centerx, 220))
        self.display_surface.blit(surf,rect)

    def update_hand(self, hand):
        terms = [('High Card: ' + str(hand[1])), 'Pair', '2 Pair', '3 of a Kind', 'Straight', 'Flush', 'Full House', '4 of a Kind', 'Straight Flush', 'Royal Flush']
        for x, term in enumerate(terms):
            if x == hand[0]:
                surf = self.font.render('Hand:', True, 'white')
                rect = surf.get_rect(center = (self.rect.centerx, 260))
                self.display_surface.blit(surf,rect)

                surf2 = surf = self.font.render(str(term), True, 'white')
                rect2 = surf2.get_rect(center = (self.rect.centerx, 290))
                self.display_surface.blit(surf2, rect2)
    
    def update(self, cash, hand):
        self.display_surface.blit(self.image, self.rect)
        self.display_surface.blit(self.title, self.title_rect)
        self.update_p_cash(cash)
        if game_data.phase == 6:
            self.update_hand(hand)
        self.display_surface.blit(self.face, self.face_rect)
        

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
