import py
import pygame
from settings import *

class MainMenu:
    def __init__(self):
        self.bg = pygame.image.load("../graphics/table/table1.jpg")
        self.bg_rect = self.bg.get_rect(topleft = (0,0))
        self.display_surface = pygame.display.get_surface()
        self.music = pygame.mixer.Sound('../music/music1.mp3')
        self.music.set_volume(.5)
        self.music.play(-1)

        #menu
        self.menu = MenuBar((500,500), ((width/2),(height/2)))

    def update(self):
        self.display_surface.blit(self.bg, self.bg_rect)

        #buttons
        self.menu.update()
    

class MenuBar(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/menu.png').convert_alpha()
        self.image_rect = self.image.get_rect(center = pos)
        self.display_surface = pygame.display.get_surface()

        #buttons
        self.five_card_button = FiveCardButton(((width/2),300), '5 Card')

    def update(self):
        self.display_surface.blit(self.image, self.image_rect)

        #buttons
        self.five_card_button.update()


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, text):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.icons = self.get_icons()
        self.image = self.icons[0]
        self.rect = self.image.get_rect(center = pos)
        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render(text, True, 'white')
        self.text_rect = self.text.get_rect(center = ((self.image.get_width() / 2), (self.image.get_height() / 2)))
        self.click_cooldown = 0
        self.active = True

    def get_icons(self):
        path = ['cardBack_blue3.png', 'cardBack_blue4.png',]
        icons = []
        for x in path:
            icon = pygame.image.load('../graphics/back/' + x).convert_alpha()
            icon = pygame.transform.rotate(icon, 90)
            icons.append(icon)
        return icons

    def input(self):
        if self.click_cooldown == 0:
            pressed = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if pressed[0] == True:
                    if self.active == True:
                        self.action()
                        self.click_cooldown += 1
                        

        elif self.click_cooldown == 30:
            self.click_cooldown = 0

        else:
            self.click_cooldown += 1
            
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.image = self.icons[1]
        else:
            self.image = self.icons[0]

    def update(self):
        self.image.blit(self.text, self.text_rect)
        self.display_surface.blit(self.image, self.rect)
        self.input()


class FiveCardButton(Button):
    def __init__(self, pos, text):
        super().__init__(pos, text)

    def action(self):
        pygame.event.post(pygame.event.Event(FiveCardButtonActive))


class ESCMenu(pygame.sprite.Sprite):
    def __init__(self, path, pos):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.display_surface = pygame.display.get_surface()

        self.roh_active = False
        self.roh = RankOfHands()

        #buttons
        self.music_button = MusicButton(((self.display_surface.get_width() / 2), ((self.display_surface.get_height() / 2) - 200)), 'Music')
        self.quit_button = QuitButton(((self.display_surface.get_width() / 2), ((self.display_surface.get_height() / 2) + 200)), 'Quit')
        self.ROH_button = ROHButton((self.rect.centerx, ((self.display_surface.get_height() / 2))), 'ROH' )

    def update(self):
        self.display_surface.blit(self.image, self.rect)
        self.music_button.update()
        self.quit_button.update()
        self.ROH_button.update()
        if self.roh_active == True:
            self.roh.update()


class MusicButton(Button):
    def __init__(self, pos, text):
        super().__init__(pos, text)

    def action(self):
        pygame.event.post(pygame.event.Event(MusicToggle))


class QuitButton(Button):
    def __init__(self, pos, text):
        super().__init__(pos, text)

    def action(self):
        pygame.event.post(pygame.event.Event(EndGame))

class ROHButton(Button):
    def __init__(self, pos, text):
        super().__init__(pos, text)

    def action(self):
        pygame.event.post(pygame.event.Event(ROH))

class RankOfHands(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../graphics/roh.png")
        self.rect = self.image.get_rect(center = ((width/2),(height/2)))
        self.display_surface = pygame.display.get_surface()

    def update(self):
        self.display_surface.blit(self.image, self.rect)