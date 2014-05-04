import pygame
class Particle(pygame.sprite.Sprite):
    '''something like an abstract class for particles'''
    proton_img = pygame.image.load('sprites/Particles.png').subsurface(0,0,30,30)#.convert_alpha()
    neutron_img = pygame.image.load('sprites/Particles.png').subsurface(0,60,30,30)#.convert_alpha()
    electron_img = pygame.image.load('sprites/Particles.png').subsurface(60,60,30,30)#.convert_alpha()
    def __init__(self,pos=(0,0),charge=0):
        pygame.sprite.Sprite.__init__(self)
        self.charge = charge
        self.image = Particle.neutron_img
        self.x,self.y = pos
    def update(self,offset):
        self.x -= offset
        self.rect.center = (self.x,self.y)
        if self.x < -60: self.kill()
class Proton(Particle):
    def __init__(self,pos):
        Particle.__init__(self,pos,1)
        self.image = Particle.proton_img.convert_alpha()
        self.rect = self.image.get_rect(center = pos)
    def update(self,offset,*args):
        Particle.update(self,offset)
class Electron(Particle):
    def __init__(self,pos):
        Particle.__init__(self,pos,-1)
        self.image = Particle.electron_img.convert_alpha()
        self.rect = self.image.get_rect(center = pos)
    def update(self,offset,*args):
        Particle.update(self,offset)
class Neutron(Particle):
    def __init__(self,pos):
        Particle.__init__(self,pos,0)
        self.image = Particle.neutron_img.convert_alpha()
        self.rect = self.image.get_rect(center = pos)
    def update(self,offset,*args):
        Particle.update(self,offset)

Particles = (Neutron,Proton,Electron)
