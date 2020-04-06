from Repo import Repo
from Service import Service



class UI:

    def __init__(self):
        self.__repo = Repo()
        self.__service = Service(self.__repo, "net.in")

    def run(self):
        pop, iter = self.popAndGen()
        best=self.__service.ACO(pop,iter)
        print("----------------")
        print("Best Path:"+str(best.path))
        print("With a distance of:"+str(best.distance))



    def popAndGen(self):
        pop=int(input("Dati populatia:"))
        gens=int(input("Iteratii:"))
        return pop,gens

