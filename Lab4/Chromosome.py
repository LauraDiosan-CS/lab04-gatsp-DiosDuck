import random
from random import randint
class Chromosome:
    def __init__(self, n):
        self.__n=n
        vec=[x for x in range(0,n)]
        random.shuffle(vec)
        self.__repres = vec
        self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r1 = randint(0,self.__n- 1)
        r2=randint(0, self.__n-1)
        if r2<r1:
            aux=r1
            r1=r2
            r2=aux
        newrepres1 = [-1]*self.__n
        newrepres2=[-1]*self.__n
        for i in range(r1,r2+1):
            newrepres1[i]=self.__repres[i]
            newrepres2[i]=c.__repres[i]
        i=(r2+1)%self.__n
        index1=(r2+1)%self.__n
        index2=(r2+1)%self.__n
        while index1!=r1 or index2!=r1:
            if index1!=r1:
                if c.__repres[i] not in newrepres1:
                    newrepres1[index1]=c.__repres[i]
                    index1=(index1+1)%self.__n
            if index2 != r1:
                if self.__repres[i] not in newrepres2:
                    newrepres2[index2] = self.__repres[i]
                    index2 = (index2 + 1) % self.__n
            i=(i+1)%self.__n
        chrom1=Chromosome(self.__n)
        chrom1.__repres=newrepres1
        chrom2=Chromosome(self.__n)
        chrom2.__repres=newrepres2
        return chrom1,chrom2

    def mutation(self):
        pos1 = randint(0, self.__n-1)
        pos2 = randint(0,self.__n-1)
        i=pos1
        j=pos2
        while i<j:
            aux=self.__repres[i]
            self.__repres[i]=self.__repres[j]
            self.__repres[j]=aux
            i+=1
            j-=1