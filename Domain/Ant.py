from random import randint


class Ant:

    def __init__(self,probParam,distance,pheromone):
        self.__probParam = probParam
        self.__repres = self.__buildPath(distance,pheromone)
        self.__distance=probParam["function"](self.__repres)


    def __str__(self):
        return str(self.__repres) + "  " + str(self.__fitness)

    @property
    def path(self):
        return self.__repres

    @property
    def distance(self):
        return self.__distance

    def __lt__(self, other):
        return self.__distance>other.distance

    def __gt__(self, other):
        return self.__distance<other.distance

    def __eq__(self, other):
        return self.__distance==other.distance

    def toList(self):
        return self.__repres

    def __buildPath(self, distance, pheromone):
        rep=[]
        rep.append(randint(self.__probParam["min"],self.__probParam["max"]))
        while len(rep)!=len(distance[0]):
            rep.append(self.__calcNext(distance[rep[-1]],pheromone[rep[-1]],rep))
        return rep

    def __calcNext(self,distance,pheromone,path):
        total=0
        chance=[]
        modified=[]
        for i in range(len(distance)):
            if i not in path:
                total+=1/distance[i]+pheromone[i]
                modified.append(1/distance[i]+pheromone[i])
            else:
                modified.append(0)
        for i in range(len(modified)):
            if modified[i] !=0:
                chance.append([i,modified[i]/total])
        chance.sort(key=lambda x:x[1])
        ch=randint(0,100)/100
        start=0;
        for num in chance:
            start+=num[1]
            if ch <=start:
                return num[0]
        return chance[-1][0]



