from Repository import Repository
from GA import GA
from GA2 import GA2

class Service:
    def __init__(self, filename,n):
        self.__n=n
        if n==1:
            self.__repository = Repository(filename)
        else:
            self.__repository=Repository(filename)

    def __rez(self, n, aux):
        bestChromosone=None
        vmin=float("inf")
        ga=GA(41,aux,n)
        ga.initialisation()
        ga.evaluation()
        for _ in range(0,6000):
            ga.oneGenerationElitism()
            chromosone=ga.bestChromosome()
            print(vmin)
            if chromosone.fitness<vmin:
                vmin=chromosone.fitness
                bestChromosone=chromosone
        return bestChromosone
    
    def __rez2(self, n, aux):
        bestChromosone=None
        vmin=float("inf")
        ga=GA2(41,aux,n)
        ga.initialisation()
        ga.evaluation()
        for _ in range(0,6000):
            ga.oneGenerationElitism()
            chromosone=ga.bestChromosome()
            print(vmin)
            if chromosone.fitness<vmin:
                vmin=chromosone.fitness
                bestChromosone=chromosone
        return bestChromosone

    def prob1(self):
        if self.__n==1:
            n, aux = self.__repository.readFromFile1()
            bestChromosone = self.__rez(n, aux)
            self.__repository.writeToFile([n, [x + 1 for x in bestChromosone.repres], bestChromosone.fitness])
        else:
            n,vec=self.__repository.readFromFile3()
            bestChromosone=self.__rez2(n,vec)
            self.__repository.writeToFile([n, [x + 1 for x in bestChromosone.repres], bestChromosone.fitness])
