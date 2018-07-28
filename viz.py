#!/usr/bin/python
import sys
import pygame
import random


def handleInput():
    #keys = pygame.key.get_pressed()
    pass

class Neighborhood:
    def __init__(self, x, y, width, height, color, id):
        self.id = id
        self.props = {'casualties':[], 'risk':[]}
        self.x = x + 1
        self.y = y + 1
        self.width = width - 2
        self.height = height - 2
        self.currentProp = "risk"

        for i in range(0, numOfDays):
            self.props['casualties'].append(random.randrange(0,100,1)/100.0)
            self.props['risk'].append(random.randrange(0,100,1) / 100.0 )
        
        
    def update(self):
        regionname = "Region%02d" % self.id
        value = simdata[currentDay-1][regionname][self.currentProp]
        #print ("Day ", currentDay, " Neighborhood ", regionname, "Property ", self.currentProp, "Value", value[0])
        self.color = SimColor.getColorForValue(float(value[0]))
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
        id = 0
        for i in range(5):
            for j in range(5):
                id+=1
                rl.append(Neighborhood(i*sWidth/5, j*sHeight/5, sWidth/5, sHeight/5, SimColor.GRAY,id))
        #rl.append(Neighborhood(50, 50, 200, 175, SimColor.RED))
        #rl.append(Neighborhood(250, 25, 100, 150, SimColor.GREEN))
        #rl.append(Neighborhood(100, 225, 150, 200, SimColor.YELLOW))
        #rl.append(Neighborhood(250, 175, 200, 200, SimColor.ORANGE))

        return rl
    
    def update(self):
        win.fill((0,0,0))
        for r in self.regionList:
            r.update()


def main(argv):
    global currentDay
    global numOfDays
    global win
    global sWidth
    global sHeight
    global simdata
    
    if len(argv) == 1:
        print("error: please specify a filename to load")

    currentDay = 1 
    numOfDays = 10

    sWidth = 1920
    sHeight = 1080
    updateInterval = 1000

    if len(argv) >= 4:
        sWidth = int(argv[2])
        sHeight = int(argv[3])
    speed = 1.0
    if len(argv) >= 5:
        speed = float(argv[4])
    win = pygame.display.set_mode((sWidth, sHeight))

    pygame.init()

    vm = VizMap()
    run = True
    i = 0
    totalrecords = 0
    simdata = []
    simday = -1
    with open(argv[1]) as f:
        
        daydata = {}
        lines = f.readlines()
        totalrecords = len(lines)
        #print(lines)
        header = True
        headervalues = []
        for line in lines:
            
            line = line.rstrip('\n')
            values = line.split('\t')
            #print (values)

            if header == True:
                header = False
                headervalues = values
                #print ("Header created")
                continue

            #print (values[0])
            if simday != int(values[0]):
                simday = int (values[0])
                simdata.append({})
                #print ("DayChanged")
            
            if values[1] in simdata[simday].keys():
                #print ("Key exists")
                pass
            else:
                #print ("Key does not exist")
                
                simdata[simday][values[1]] = { headervalues[2] : [], headervalues[3] : [],headervalues[4] : [],headervalues[5] : []}

            # print (simdata)
            # print (simday)
            # print (values[1])
            # print (simdata[simday])
            #day	region	casualties	evacuated	shelter	risk
            simdata[simday][values[1]][headervalues[2]].append(values[2])
            simdata[simday][values[1]][headervalues[3]].append(values[3])
            simdata[simday][values[1]][headervalues[4]].append(values[4])
            simdata[simday][values[1]][headervalues[5]].append(values[5])

    # i  = 0
    # for daydata in simdata:
    #     i+=1
    #     print("day ", i)
    #     print (n_data)

    numOfDays = simday 
    pygame.time.delay(2000)
    i = 0.0
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        handleInput()
        vm.update()        

        if i == 0.0:
            pygame.display.set_caption("Vizualization Day %d" % currentDay)
            if currentDay < numOfDays :
                currentDay += 1
            else: 
                currentDay = 1
                exit(0)
        if i < 10.0 / speed: 
            i += 1.0
        else:
            i = 0.0

        pygame.display.update()


if __name__ == "__main__":
    #print len(sys.argv)
    #print sys.argv
    main(sys.argv)
    