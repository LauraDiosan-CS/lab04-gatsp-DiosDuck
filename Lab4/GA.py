from random import randint
from Chromosome import Chromosome


class GA:
    def __init__(self,popSize,matrice,n):
        self.__popSize=popSize
        self.__matrice=matrice
        self.__n=n
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        for _ in range(0, self.__popSize):
            c = Chromosome(self.__n)
            self.__population.append(c)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__fitness(c.repres)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = randint(0, self.__popSize-1)
        pos2 = randint(0, self.__popSize-1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        newPop = []
        while len(newPop)<self.__popSize:
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            chrom1,chrom2 = p1.crossover(p2)
            chrom1.mutation()
            chrom2.mutation()
            newPop.append(chrom1)
            newPop.append(chrom2)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__popSize - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            chrom1, chrom2 = p1.crossover(p2)
            chrom1.mutation()
            chrom2.mutation()
            newPop.append(chrom1)
            newPop.append(chrom2)
        self.__population = newPop
        self.evaluation()

    def __fitness(self,vec):
        fitness=0
        for i in range(0,self.__n-1):
            fitness+=self.__matrice[vec[i]][vec[i+1]]
        fitness += self.__matrice[vec[-1]][vec[0]]
        return fitness