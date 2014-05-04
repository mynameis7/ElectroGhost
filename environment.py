import pygame,random
from constants import Constants
class Generator(pygame.sprite.Sprite):
    proton_gen = pygame.image.load('sprites/Proton_Gen.png')
    neutron_gen = pygame.image.load('sprites/Neutron_Gen.png')
    electron_gen = pygame.image.load('sprites/Electron_Gen.png')
    random_gen = pygame.image.load('sprites/Random_Gen.png')
    def __init__(self,pos=(0,0),flip=1):
        pygame.sprite.Sprite.__init__(self)
        self.image=Generator.random_gen.convert_alpha()
        self.rect=self.image.get_rect(center=pos)
        self.flip = flip
        self.x,self.y = pos
        self.timer = 60
    def update(self,offset):
        self.x -= offset
        self.rect.center = (self.x,self.y)
        if self.timer <= 0:
            self.timer = 60
            spark_evt = pygame.event.Event(Constants.ADD_SPARK,{'pos':self.rect.center,'charge':self.charge,'color':self.color,
                                                                'vel':self.flip*3})
            pygame.event.post(spark_evt)
        self.timer -= 1
        if self.x < -60:
            self.kill()
class ProtonGenerator(Generator):
    def __init__(self,pos=(0,0),flip=1):
        Generator.__init__(self,pos,flip)
        self.image = Generator.proton_gen.convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.charge = 1
        self.color =1
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image,0,1)
    def update(self,offset,*args):
        Generator.update(self,offset)
class ElectronGenerator(Generator):
    def __init__(self,pos=(0,0),flip=1):
        Generator.__init__(self,pos,flip)
        self.image = Generator.electron_gen.convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.charge = -1
        self.color = 2
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image,0,1)
    def update(self,offset,*args):
        Generator.update(self,offset)
class NeutronGenerator(Generator):
    def __init__(self,pos=(0,0),flip=1):
        Generator.__init__(self,pos,flip)
        self.image = Generator.neutron_gen.convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.charge = 0
        self.color = 0
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image,0,1)
    def update(self,offset,*args):
        Generator.update(self,offset)
class RandomGenerator(Generator):
    def __init__(self,pos=(0,0),flip=1):
        Generator.__init__(self,pos)
        self.image = Generator.proton_gen.convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.charge = 0
        self.color = 4
        if self.flip == -1:
            self.image = pygame.transform.flip(self.image,0,1)
    def update(self,offset,*args):
        self.charge = random.randrange(3)-1
        Generator.update(self,offset)
Generators = (NeutronGenerator,ProtonGenerator,ElectronGenerator,RandomGenerator)


class Spark(pygame.sprite.Sprite):
    def __init__(self,pos=(0,0),charge=0,color=0,vel=5):
        pygame.sprite.Sprite.__init__(self)
        if color == 0:
            self.images = self.load_sliced_sprites(30,30,'sprites/YellowSpark.png')
        elif color == 1:
            self.images = self.load_sliced_sprites(30,30,'sprites/RedSpark.png')
        elif color == 2:
            self.images = self.load_sliced_sprites(30,30,'sprites/BlueSpark.png')
        else:
            self.images = self.load_sliced_sprites(30,30,'sprites/GreenSpark.png')
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        self.charge = charge
        self.x,self.y = pos
        self.vel = vel
    def load_sliced_sprites(self,width,height,filename):
        images = []
        master_image = pygame.image.load(filename).convert_alpha()
        m_width, m_height = master_image.get_size()
        for i in xrange(int(m_width/width)):
            images.append(master_image.subsurface((i*width,0,width,height)))
        return images
    def update(self,offset,*args):
        self.x -= offset
        self.y -= self.vel
        self.rect.center = (self.x,self.y)
        if self.x < -60 or self.y > Constants.HEIGHT+60 or self.y<-60:
            self.kill()
