from copy import deepcopy

from Domain.Population import Population
from Repo import Repo
from Utils import getParam


class Service:

    def __init__(self,repo,filePath):
        self.repo=repo
        self.filePath=filePath

    # load a network
    def loadNetwork(self):
        return self.repo.readNet(self.filePath)


    def generateElitism(self,popSize,gens):
        probParam, param = getParam(popSize)
        pop = Population(param, probParam)
        pop.initialisation()
        pop.evaluation()

        #randomPop = deepcopy(pop)
        # Prints and plots the Random Generated Comunity
        # print(pop.bestChromosome().toList())
        # self.plotCommunities(pop.bestChromosome().toList())
        # print(modularity(pop.bestChromosome().toList()))

        # prints and plots the Best Comunity generated using elitism
        bestChr=[]
        bestChr.append(deepcopy(pop.bestChromosome()))
        for _ in range(gens):
            pop.oneGenerationElitism()
            bestChr.append(deepcopy(pop.bestChromosome()))
        # print(pop.bestChromosome().toList())
        # self.plotCommunities(pop.bestChromosome().toList())
        # print(modularity(pop.bestChromosome().toList()))
        return bestChr


    def generateRares(self,popSize,gens):
        probParam, param = getParam(popSize)
        pop = Population(param, probParam)
        pop.initialisation()
        pop.evaluation()

        # randomPop = deepcopy(pop)
        # Prints and plots the Random Generated Comunity
        # print(pop.bestChromosome().toList())
        # self.plotCommunities(pop.bestChromosome().toList())
        # print(modularity(pop.bestChromosome().toList()))

        # prints and plots the Best Comunity generated using elitism
        bestChr = []
        bestChr.append(deepcopy(pop.bestChromosome()))
        for _ in range(gens):
            pop.raresGeneration()
            bestChr.append(deepcopy(pop.bestChromosome()))
        # print(pop.bestChromosome().toList())
        # self.plotCommunities(pop.bestChromosome().toList())
        # print(modularity(pop.bestChromosome().toList()))
        return bestChr