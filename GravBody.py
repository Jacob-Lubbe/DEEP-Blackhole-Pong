import pygame
import numpy as np
from constants import g_constant, null_vector, mass_constant

class GravBody(pygame.sprite.Sprite):
    '''A GravBody object that can interact gravitationally
    Returns: GravBody object
    Functions: draw, update
    Attributes: area, vector'''

    def __init__(self, name, image, scale, position=null_vector, velocity=null_vector, mass=mass_constant):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
        	pygame.image.load(image),
        	scale
        	)
        self.scale = np.array(scale)
        self.name = name
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.position = np.array(position, dtype='float64')
        self.velocity = np.array(velocity, dtype='float64')
        self.mass = mass
        
    def calc_distance(self,other):
        '''Calculates the distance to another GravBody)'''
        return (np.sum(self.position-other.position)**2)**.5
        
    def calc_unit_displacement_vector(self,other):
        '''Calculates the unit displacement vecto to another GravBody'''
        return (other.position - self.position)/self.calc_distance(other)

    def calc_gravity(self, other):
        '''Calculates the gravitational force to another GravBody'''
        r = self.calc_distance(other)
        unit_displacement_vector = self.calc_unit_displacement_vector(other)       
        fg = g_constant*self.mass*other.mass/r**1*unit_displacement_vector
        return fg
        
        
        
    def update(self, timestep = 1, force=null_vector, gbodies=[]):
        '''takes a force and updates the position'''
        self.velocity += force/self.mass*timestep
        self.position = self.velocity*timestep + self.position
        
    def draw(self):
    	self.screen.blit(self.image, self.position-self.scale/2)
    	
    def __repr__(self):
        return '''GravBody: {} mass {} pos {} vel {}'''.format(self.name, self.mass, self.position, self.velocity)
