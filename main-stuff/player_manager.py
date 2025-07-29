''' PLAYER FILE - MANAGES THE PLAYER '''
''' IMPORTS '''
#need for rotating sprite
import pygame
#needed for getting rotation angle
import math
#needed for bullets
import bullet

''' PLAYER CLASS '''
class Player:
    def __init__(self, sprite, surface):
        self._sprite = sprite
        self._draw_sprite = self._sprite
        self._surface = surface
        self._angle = 0
        self._bullet = None
        self.update_rect()

    def player_rotate(self, mouse_pos):
        ''' Rotates the player given a mouse position '''
        #gets the distance of the side adjacent to the neccessary angle
        adjacent_dist = mouse_pos[0] - self._surface.get_width() // 2
        #gets the distance of the side opposite to the neccessary angle
        opposite_dist = mouse_pos[1] - self._surface.get_height() // 2
        #gets the tangent as a degree measurement with an inverse tangent
        self._angle = math.degrees(math.atan2(opposite_dist, adjacent_dist))
        #sets the draw sprite to a modified version of the og sprite
        self._draw_sprite = pygame.transform.rotate(self._sprite, -self._angle - 90)
        #update the rect
        self.update_rect()
    
    def update_rect(self):
        ''' Updates the rect of the player after a rotation '''
        self._collison_rect = self._sprite.get_rect()
        self._collison_rect.center = (self._surface.get_width()/2, self._surface.get_height()/2)
        self._rect = self._draw_sprite.get_rect()
        self._rect.center = (self._surface.get_width()/2, self._surface.get_height()/2)
    
    def spawn_bullet(self):
        ''' Spawns a bullet '''
        self._bullet = bullet.Bullet(self._rect.center[0], self._rect.center[1], self._angle, self._surface)

    def draw_self(self):
        ''' Draws the player to the screen '''
        pygame.draw.rect(self._surface, (255, 0, 0), self._collison_rect)
        self._surface.blit(self._draw_sprite, (self._rect.x, self._rect.y))