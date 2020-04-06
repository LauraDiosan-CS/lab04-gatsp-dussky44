

from Domain.Colony import Colony
from Utils import getParam


class Service:

    def __init__(self,repo,filePath):
        self.repo=repo
        self.filePath=filePath

    # load a network
    def loadNetwork(self):
        return self.repo.readNet(self.filePath)



    def ACO(self,popSize,iterations):
        probParam, param = getParam(popSize)
        col=Colony(param, probParam)
        best=col.nextInteration(iterations)
        return best