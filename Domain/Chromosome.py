from random import randint, choice



class Chromosome:

    def __init__(self,probParam=None):
        self.__probParam = probParam
        self.__repres = []
        all=list(range(probParam["min"],probParam["max"]))
        while all:
            gene=choice(all)
            all.remove(gene)
            self.__repres.append(gene)
        self.__fitness=probParam["function"](self.__repres)

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, c=[]):
        self.__repres=c

    @fitness.setter
    def fitness(self, f=0.0):
        self.__fitness=f


    def crossover(self,ot):
        offspring=[-1]*self.__probParam["noNode"]
        overflow=[]
        for i in range(self.__probParam["noNode"]):
            gene=choice([self.repres,ot.repres])
            if offspring[gene.index(i)]==-1:
                offspring[gene.index(i)]=i
            else:
                overflow.append(i)
        while overflow:
            offspring[offspring.index(-1)]=overflow.pop()
        c=Chromosome(self.__probParam)
        c.repres=offspring
        return c

    def mutation(self):
        pos1=randint(0,self.__probParam["noNode"]-1)
        pos2=randint(0,self.__probParam["noNode"]-1)
        self.__repres[pos1],self.__repres[pos2] = self.__repres[pos2],self.__repres[pos1]


    def __str__(self):
        return str(self.__repres) + " Fitness: " + str(self.__fitness)

    def __lt__(self, other):
        return self.__fitness>other.fitness

    def __gt__(self, other):
        return self.__fitness<other.fitness

    def __eq__(self, other):
        return self.__fitness==other.fitness

    def toList(self):
        return self.__repres

