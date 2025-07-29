''' WALL FILE - MANAGES WALLS '''
''' IMPORTS '''
import pygame

class Wall_Tile:
    def __init__(self, sprite, surface, pos):
        self._sprite = sprite
        self._surface = surface
        self._rect = pygame.Rect(pos[0], pos[1], self._sprite.get_width(), self._sprite.get_height())
    
    def draw_self(self):
        ''' Draws the sprite '''
        self._surface.blit(self._sprite, (self._rect.x, self._rect.y))