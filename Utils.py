from math import sqrt


def calcPath(path):
    param=loadNetwork()
    sum=0
    for i in range(1,len(path)):
        sum+=int(param[path[i-1]][path[i]])
    return sum


def readDistNet(fileName):
    coord=[]
    with open(fileName) as f:
        number=int(f.readline())
        for n in range(number):
            coord.append(f.readline().strip().split(" "))
    cities=[]
    for n in range(number):
        line=[]
        for i in range(number):
            line.append(calcDistance(coord[n],coord[i]))
        cities.append(line)
    return cities

def readNet(fileName):
    cities = []
    with open(fileName) as f:
        number = int(f.readline())
        for n in range(number):
            cities.append(f.readline().strip().split(","))
    ints=[]
    for city in cities:
        ints.append(list(map(lambda x:int(x),city)))

    return ints


def loadNetwork():
    #return readNet("test2.txt")
    #return readNet("test1.txt")
    #return readNet("nodes.txt")
    return readNet("easy_01_tsp.txt")
    #return readDistNet("berlin.txt")
    #return readDistNet("hardE.txt")


#Set the default params from here
def getParam(popSize):
    probParam={}
    Param={}
    net=loadNetwork()
    noNodes=len(net)
    probParam["min"]=0
    probParam["max"]=noNodes-1
    probParam["noNode"]=noNodes
    Param["popSize"]=popSize
    probParam['function']=calcPath
    return probParam,Param

def calcDistance(p1,p2):
    return sqrt((float(p1[1])-float(p2[1]))**2+(float(p1[2])-float(p2[2]))**2)