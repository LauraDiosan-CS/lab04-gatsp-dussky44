from Repo import Repo
from Service import Service
from collections import Counter
from Utils import calcPath


class UI:

    def __init__(self):
        self.__repo = Repo()
        self.__service = Service(self.__repo, "net.in")

    def run(self):
        self.printMenu()
        choice=int(input("Alegeti:"))
        while choice != 0:
            if choice== 1:
                pop, gens = self.popAndGen()
                bestChr = self.__service.generateElitism(pop, gens)
                self.printBest(bestChr)
            else:
                pop, gens = self.popAndGen()
                bestChr=self.__service.generateRares(pop,gens)
                self.printBest(bestChr)
            self.printMenu()
            choice=int(input("Alegeti:"))


    def printMenu(self):
        print("1.Generate using Elitism")
        print("2.Generate using Rares's own unstable algorithm")

    def popAndGen(self):
        pop=int(input("Dati populatia:"))
        gens=int(input("Generatii:"))
        return pop,gens

    def printBest(self,bestChr):
        print("---------------------")
        i=0;
        for chr in bestChr:
            self.printAndPlot(chr,i)
            i+=1

        print("---------------------")
        print("Best TSP Path:"+ str([x+1 for x in chr.toList()]))
        print("With a total cost of:" + str(calcPath(chr.toList())))
        print("---------------------")
        print("---------------------")

    def printAndPlot(self,chr,gen):
        print("Generation "+ str(gen))
        print("Best Path of this Generation:"+ str([x+1 for x in chr.toList()]))
        print("Best fitness of this Generation:" + str(calcPath(chr.toList())))
        print(" ")
