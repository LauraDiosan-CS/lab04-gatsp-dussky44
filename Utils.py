
import warnings

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def calcPath(path):
    param=loadNetwork()
    sum=0
    for i in range(1,len(path)):
        sum+=int(param[path[i-1]][path[i]])
    return sum


def readNet(fileName):
    cities = []
    with open(fileName) as f:
        number = int(f.readline())
        for n in range(number):
            cities.append(f.readline().strip().split(","))
    return cities


def loadNetwork():
    return readNet("easy_01_tsp.txt")


#Set the default params from here
def getParam(popSize):
    probParam={}
    Param={}
    net=loadNetwork()
    noNodes=len(net)
    probParam["min"]=0
    probParam["max"]=noNodes
    probParam["noNode"]=noNodes
    Param["popSize"]=popSize
    probParam['function']=calcPath
    return probParam,Param