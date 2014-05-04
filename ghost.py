import pygame,math
from pygame.locals import *
from constants import Constants
BLACK = (0,0,0)
WHITE = (255,255,255)
class Ghost(pygame.sprite.Sprite):
    def __init__(self,pos=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.images = self.load_sliced_sprites(60,60,'sprites/GhostStrip.png')
        self.frame_cnt = len(self.images)
        self.frame = 0
        self.image = self.images[0]
        self.curr = pygame.time.get_ticks
        self.start = self.curr()
        self.rect = self.image.get_rect(center = pos)

        self.stability = 100
        
        #index: 0=neutron, 1=proton,2(-1)=electron
        self.collected = [1,1,1]
        self.velocity = [0,0]
        self.x,self.y = pos
    def load_sliced_sprites(self,width,height,filename):
        images = []
        master_image = pygame.image.load(filename).convert()
        master_image.set_colorkey(BLACK)
        m_width, m_height = master_image.get_size()
        for i in xrange(int(m_width/width)):
            images.append(master_image.subsurface((i*width,0,width,height)))
        return images
    def updateImage(self):
        advFrame = (self.curr()/100)%self.frame_cnt
        if self.frame != advFrame:
            self.frame = advFrame
            self.image = self.images[advFrame]
    def updateVelocity(self):
        if abs(self.velocity[0])>0.25:
            self.velocity[0] *= 0.95
        if abs(self.velocity[1])>0.25:
            self.velocity[1] *= 0.95
        if abs(self.velocity[0])<=0.25 and self.velocity[0] != 0:
            self.velocity[0] = 0
        if abs(self.velocity[1])<=0.25 and self.velocity[1] != 0:
            self.velocity[1] = 0
        if abs(self.velocity[0])>7:
            self.velocity[0] = math.copysign(7,self.velocity[0])
        if abs(self.velocity[1])>7:
            self.velocity[1] = math.copysign(7,self.velocity[1])
    def angle_to_point(self,pos):
        x1,y1 = self.rect.center
        x2,y2 = pos
        angle = math.atan2(y1-y2,x2-x1)
        return angle
    def setVelocity(self,vel):
        self.velocity = list(vel)
    def move(self):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        self.rect.center = (self.x,self.y)
    def draw(self,surface):
        surface.blit(self.image,self.rect)
    def update(self,offset):
        self.updateImage()
        self.updateVelocity()
        self.x -= offset
        self.move()
        self.rect.clamp_ip(Constants.screen_rect)
