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
        self._x_vel = math.cos(angle * (2 * math.pi / 360)) * 10
        self._y_vel = math.sin(angle * (2 * math.pi / 360)) * 10

    def bullet_movement(self):
        ''' Moves the bullet '''
        #adds to the center x coordinate
        self._center[0] += self._x_vel
        #adds to the center y coordinate
        self._center[1] += self._y_vel

        #check for collision on the x axis
        if self._center[0] - self._r < 0 or self._center[0] + self._r > self._surface.get_width():
            #reverse the velocity
            self._x_vel = -self._x_vel

        #check for collision on the y axis
        if self._center[1] - self._r < 0 or self._center[1] + self._r > self._surface.get_height():
            #reverse the velocity
            self._y_vel = -self._y_vel

    def draw_bullet(self):
        ''' Draws the bullet '''
        pygame.draw.circle(self._surface, (255, 0, 0), self._center, self._r)