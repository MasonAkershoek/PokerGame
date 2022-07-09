import pygame
from settings import *
import game_data


class Button(pygame.sprite.Sprite):
    def __init__(self, size, pos, box_color, text_color, text, text_size):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(None, text_size)
        self.icons = self.get_icons()
        self.image = self.icons[0]
        self.color = box_color
        self.rect = self.image.get_rect(center = pos)
        self.text = self.font.render(text, True, text_color)
        self.text_rect = self.text.get_rect(center = ((self.image.get_width() / 2),(self.image.get_height() / 2)))
        self.size = size
        self.click_cooldown = 0
        self.active = True

    def  get_icons(self):
        path = ['chipBlueWhite.png', 'chipBlue.png', 'chipBlackWhite.png']
        icons = []
        for x in path:
            icon = pygame.image.load('../graphics/' + x)
            icon = pygame.transform.scale2x(icon)
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
        self.onoff()
        self.input()
        self.image.blit(self.text, self.text_rect)
        self.display_surface.blit(self.image, self.rect)


class DealButton(Button):
    def __init__(self, size, pos, box_color, text_color, text, text_size):
        super().__init__(size, pos, box_color, text_color, text, text_size)

    def onoff(self):
        if game_data.phase == 1 or game_data.phase == 3 or game_data.phase == 6:
            self.active = True
        else:
            self.active = False
    
    def action(self):
        pygame.event.post(pygame.event.Event(DealButtonActive))


class BetButton(Button):
    def __init__(self, size, pos, box_color, text_color, text, text_size):
        super().__init__(size, pos, box_color, text_color, text, text_size)

    def onoff(self):
        if game_data.phase == 3 or game_data.phase == 6:
            self.active = True
        else:
            self.active = False
    
    def action(self):
        pygame.event.post(pygame.event.Event(BetButtonActive))


class FoldButton(Button):
    def __init__(self, size, pos, box_color, text_color, text, text_size):
        super().__init__(size, pos, box_color, text_color, text, text_size)

    def onoff(self):
        if game_data.phase == 3 or game_data.phase == 6:
            self.active = True
        else:
            self.active = False
    
    def action(self):
        pygame.event.post(pygame.event.Event(FoldButtonActive))
        



