from pygame.event import Event
from constants import Constants
import particles
import environment
class Timer(object):
    def __init__(self):
        self.curr=0
    def update(self):
        self.curr+=1
class EventQueue(object):
    def __init__(self,eventlist=[]):
        if eventlist:
            self.eventlist = self.load(eventlist)
    def load(self,eventlist):
        '''load the eventlist into the queue. overwrites previous eventlist.
            event format should be: "time:object:position"
            object:
            \tparticles: 0-neutron, 1-proton, 2-electron
            \tBlocks: 3-block, 4-(+)magnet, 5-(-)magnet
            \tGenerators: 6x-neutron generator, 7x-proton generator, 8x-electron generator, 9x-random generator
            \t\t\t x: 0-point up, 1-point down'''
        events = []
        for event in eventlist:
            event = event.strip()
            event = event.split(':')
            event_ID = 0
            pos = eval(event[2])
            pos = pos[0]+30,pos[1]
            _type = None
            data = None
            if event[1] in ('0','1','2'):
                event_ID = Constants.ADD_PARTICLE
                _type = particles.Particles[eval(event[1])]
                data = {'time':eval(event[0]),'particle':_type,'pos':pos}
            elif event[1] in ('3','4','5'):
                event_ID = Constants.ADD_BLOCK
                _type = None
                data = {'time':eval(event[0]),'particle':_type,'pos':pos}
            elif event[1] in ('60','70','80','90','61','71','81','91'):
                print event[1]
                event_ID = Constants.ADD_GENERATOR
                _type = environment.Generators[eval(event[1])/10-6]
                fp=1
                if eval(event[1])%2:
                    fp=-1
                data = {'time':eval(event[0]),'particle':_type,'pos':pos,'flip':fp}
            events.append(Event(event_ID,data))
        self.eventlist = events
    def pop(self):
        '''remove the first event on the event queue, and return it'''
        if len(self.eventlist)>=2:
            val = self.eventlist[0]
            self.eventlist = self.eventlist[1:]
            self.last = val
            return val
        elif len(self.eventlist) == 1:
            val = self.eventlist[0]
            self.eventlist = []
            self.last = val
            return val
        else:
            return None
    def get_next(self):
        '''returns the next event from the event queue without removing it'''
        if self.eventlist:
            return self.eventlist[0]
        return None
    _next = property(get_next)
    
    def get_size(self):
        '''returns the number of events left in the event queue'''
        return len(self.eventlist)
    size = property(get_size)
