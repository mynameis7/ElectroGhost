
import pygame,math
from pygame.locals import *
from constants import Constants
from ghost import Ghost
import particles
import gameTime
import environment
def test():
    '''test function for proof of concept of the new level system'''
    #new level system is generated from a file, while the game is running as opposed to all at once.
    def drawDiagnostic(surf,**kwargs):
        f = pygame.font.Font(None,20)
        h = 0
        for i in kwargs:
            outstr = '{0}:{1}'.format(i,kwargs[i])
            font_obj = f.render(outstr,False,Constants.WHITE)
            surf.blit(font_obj,(Constants.WIDTH-font_obj.get_width(),h*20))
            h += 1
    pygame.init()
    screen = pygame.display.set_mode((Constants.WIDTH,Constants.HEIGHT))
    player = Ghost((50,300))
    parts = pygame.sprite.Group()
    gens = pygame.sprite.Group()
    sparks = pygame.sprite.Group()
    num = 0
    off = .75
    timer = gameTime.Timer()
    fpsClock = pygame.time.Clock()
    events = []
    for i in xrange(100):
        for j in xrange(10):
            #pos = (i*30+200,j*30+100)
            pos = (Constants.WIDTH,j*30+100)
            out = '{0}:{1}:{2}'.format((i*30+200)/off,(num%4+6)*10+num%2,pos)
            events.append(out)
            num += 1
    timeline = gameTime.EventQueue()
    timeline.load(events)
    while True:
        screen.fill(Constants.BLACK)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                SystemExit
            elif event.type == MOUSEBUTTONDOWN:
                angle = player.angle_to_point(event.pos)
                vel = [7*math.cos(angle),-7*math.sin(angle)]
                player.setVelocity(vel)
            elif event.type == Constants.ADD_PARTICLE:
                parts.add(event.particle(event.pos))
            elif event.type == Constants.ADD_GENERATOR:
                gens.add(event.particle(event.pos,flip=event.flip))
            elif event.type == Constants.ADD_SPARK:
                sparks.add(environment.Spark(event.pos,event.charge,event.color,event.vel))
        pygame.event.clear()
        if timeline._next:
            while timeline._next and timer.curr>timeline._next.time:
                pygame.event.post(timeline.pop())
        parts.update(off)
        parts.draw(screen)
        gens.update(off)
        gens.draw(screen)
        sparks.update(off)
        sparks.draw(screen)
        player.update(off)
        player.draw(screen)
        coll = pygame.sprite.spritecollideany(player,parts,pygame.sprite.collide_mask)
        if coll:
            player.collected[coll.charge]+=1
            coll.kill()
        drawDiagnostic(screen,velocity=player.velocity,neutrons=player.collected[0],protons=player.collected[1],electrons=player.collected[2],particle_cnt=len(parts))
        pygame.display.update()
        fpsClock.tick(60)
        timer.update()
        
def main():
    pygame.init()
    pygame.display.set_mode((Constants.WIDTH,Constants.HEIGHT))
    
if __name__ == '__main__':
    test()
