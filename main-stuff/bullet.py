''' BULLET FILE - MANAGES BULLETS '''
''' IMPORTS '''
#needed for visuals
import pygame
#needed for calculating the trajectories
import math

class Bullet:
    def __init__(self, x, y, angle, surface):
        self._surface = surface
        self._center = [x, y]
        self._r = 20
        self._rect = pygame.Rect(self._center[0] - self._r, self._center[1] - self._r, self._r * 2, self._r * 2)
        self._x_vel = math.cos(angle * (2 * math.pi / 360)) * 10
        self._y_vel = math.sin(angle * (2 * math.pi / 360)) * 10
    
    def update_rect(self):
        ''' Updates bullet rect '''
        self._rect = pygame.Rect(self._center[0] - self._r, self._center[1] - self._r, self._r * 2, self._r * 2)

    def find_wall_collisons(self, walls):
        ''' Finds wall collisons '''
        #creates an empty list to store the collisons
        collisons = []
        #iterates over all the walls
        for wall in walls:
            if self._rect.colliderect(wall._rect):
                collisons.append(wall)
        return collisons

    def bullet_movement(self, walls):
        ''' Moves the bullet '''
        #finds all wall collisons
        collisons = self.find_wall_collisons(walls)

        #x-axis collision
        for wall in collisons:
            temp_rect = self._rect
            temp_rect.x += -self._x_vel
            if temp_rect.colliderect(wall._rect) == False:
                self._x_vel = -self._x_vel
        
        #y-axis collison
        for wall in collisons:
            temp_rect = self._rect
            temp_rect.y += -self._y_vel
            if temp_rect.colliderect(wall._rect) == False:
                self._y_vel = -self._y_vel

        #check for collision on the x axis
        if self._center[0] - self._r < 0 or self._center[0] + self._r > self._surface.get_width():
            #reverse the velocity
            self._x_vel = -self._x_vel

        #check for collision on the y axis
        if self._center[1] - self._r < 0 or self._center[1] + self._r > self._surface.get_height():
            #reverse the velocity
            self._y_vel = -self._y_vel

        #adds to the center x coordinate
        self._center[0] += self._x_vel
        #adds to the center y coordinate
        self._center[1] += self._y_vel
        #updates rect
        self.update_rect()

    def draw_bullet(self):
        ''' Draws the bullet '''
        pygame.draw.rect(self._surface, (0, 255, 0), self._rect, 1)
        pygame.draw.circle(self._surface, (255, 0, 0), self._center, self._r)