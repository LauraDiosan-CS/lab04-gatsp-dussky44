from random import randint

from Domain.Ant import Ant
from Utils import loadNetwork


class Colony:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__distance = loadNetwork()
        self.__pheromone = self.firstPheromone()
        self.__problParam = problParam
        self.__ants = []
        self.generateAnts()

    def firstPheromone(self):
        pheromone = []
        for i in range(len(self.__distance)):
            ph = [1] * len(self.__distance)
            ph[i] = 0
            pheromone.append(ph)
        return pheromone

    @property
    def ants(self):
        return self.__ants

    def generateAnts(self):
        for _ in range(0, self.__param['popSize']):
            c = Ant(self.__problParam, self.__distance, self.__pheromone)
            self.__ants.append(c)

    def bestAnt(self):
        best = self.__ants[0]
        for c in self.__ants:
            if c > best:
                best = c
        return best

    def adjustPheromon(self):
        b=[]
        for a in self.__pheromone:
            b.append(list(map(lambda x : x*0.8,a)))
        self.__pheromone=b
        for ant in self.__ants:
            for i in range(len(ant.path)-1):
                self.__pheromone[i][i+1]=1/ant.distance
                self.__pheromone[i+1][i]=1/ant.distance

    def dinamizare(self):
        a=randint(self.__problParam["min"],self.__problParam["max"])
        b=randint(self.__problParam["min"],self.__problParam["max"])
        while(a!=b):
            b=randint(self.__problParam["min"],self.__problParam["max"])
        self.__distance[a][b]=self.__distance[b][a]=99999
        self.__pheromone[a][b]=self.__pheromone[b][a]=0

    def nextInteration(self,iterations):
        for i in range(iterations):
            print("Cel mai bun traseu din iteratia "+str(i)+":"+str(self.bestAnt().distance))
            self.adjustPheromon()
            if i%2==0:
                self.dinamizare()
            self.generateAnts()
        return self.bestAnt()


