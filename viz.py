import sys
import pygame
import random

def handleInput():
    #keys = pygame.key.get_pressed()
    pass

class Neighborhood:
    def __init__(self, x, y, width, height, color):
        self.props = {'casualties':[], 'risk':[]}
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.currentProp = "risk"

        for i in range(0, numOfDays):
            self.props['casualties'].append(random.randrange(0,100,1)/100.0)
            self.props['risk'].append(random.randrange(0,100,1) / 100.0 )
        
    def update(self):
        self.color = SimColor.getColorForValue(self.props[self.currentProp][currentDay - 1])
        rect = pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        if rect.collidepoint(pygame.mouse.get_pos()):
            s = pygame.Surface((self.width,self.height), pygame.SRCALPHA)
            s.set_alpha(127)
            s.fill((127, 127, 127))                        
            win.blit(s, (self.x, self.y))  

class SimColor:
    RED = (255,0,0)
    ORANGE = (255,165,0)
    YELLOW = (255,255,0)
    LGREEN = (0,127,0)
    GREEN = (0,255,0)
    GRAY = (127, 127, 127)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    @classmethod
    def getColorForValue(cls,val):
        if val <= 0.2:
            return cls.RED
        elif val <= 0.4:
            return cls.ORANGE
        elif val <= 0.6:
            return  cls.YELLOW
        elif val <= 0.8:
            return cls.LGREEN
        elif val <= 1.0:
            return cls.GREEN

class VizMap:

    def pygameInit(self):
        pygame.display.set_caption("Vizualization")

    def __init__(self):
        

        self.pygameInit()
        self.regionList = self.getRegions()
        
    def getRegions(self):
        rl = []
        rl.append(Neighborhood(50, 50, 200, 175, SimColor.RED))
        rl.append(Neighborhood(250, 25, 100, 150, SimColor.GREEN))
        rl.append(Neighborhood(100, 225, 150, 200, SimColor.YELLOW))
        rl.append(Neighborhood(250, 175, 200, 200, SimColor.ORANGE))

        return rl
    
    def update(self):
        win.fill((0,0,0))
        for r in self.regionList:
            r.update()


def main():
    global currentDay
    global numOfDays
    global win
    
    currentDay = 1 
    numOfDays = 10

    sWidth = 500
    sHeight = 500
    updateInterval = 1000

    win = pygame.display.set_mode((sWidth, sHeight))

    pygame.init()

    vm = VizMap()
    run = True
    i = 0

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        handleInput()
        vm.update()        

        if i == 0:
            print "day = %s", currentDay
            if currentDay < numOfDays :
                currentDay += 1
            else: 
                currentDay = 1
        if i < 10:
            i += 1
        else:
            i = 0

        pygame.display.update()


if __name__ == "__main__":
    print len(sys.argv)
    print sys.argv
    main()
    