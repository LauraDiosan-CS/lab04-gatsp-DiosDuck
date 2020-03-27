class Repository:
    def __init__(self,filename):
        self.__filename=filename

    def readFromFile1(self):
        file = self.__filename
        matrice = []
        with open(file) as f:
            n = [int(x) for x in next(f).split()][0]
            for lines in f:
                matrice.append([int(x) for x in lines.split(",")])
        return [n, matrice]

    def readFromFile3(self):
        file = self.__filename
        vec=[]
        with open(file) as f:
            f.readline()
            f.readline()
            f.readline()
            n=int(f.readline().split(" ")[2])
            f.readline()
            f.readline()
            i=0
            while i<n:
                lines=f.readline()
                vec.append([int(x) for x in lines.split(" ")])
                i+=1
        return [n,vec]

    def readFromFile2(self):
        file = self.__filename
        matrice = []
        with open(file) as f:
            n = [int(x) for x in next(f).split()][0]
            i=0
            while i<n:
                matrice.append([int(x) for x in next(f).split(",")])
                i+=1
            a = [int(x) for x in next(f).split()][0]
            b = [int(x) for x in next(f).split()][0]
        return [n,matrice,a,b]

    def writeToFile3(self,data):
        file = self.__filename.split(".txt")[0] + "_solution.txt"
        n1 = data[0]
        vec1 = data[1]
        sum1 = data[2]
        n2=data[3]
        vec2=data[4]
        sum2=data[5]
        with open(file, 'w') as writer:
            writer.write(str(n1) + "\n")
            writer.write(str(vec1[0]))
            i = 1
            while i < len(vec1):
                writer.write("," + str(vec1[i]))
                i += 1
            writer.write("\n" + str(sum1)+"\n")
            writer.write(str(n2) + "\n")
            writer.write(str(vec2[0]))
            i = 1
            while i < len(vec2):
                writer.write("," + str(vec2[i]))
                i += 1
            writer.write("\n" + str(sum2) + "\n")

    def writeToFile(self,data):
        file=self.__filename.split(".txt")[0]+"_solution.txt"
        n=data[0]
        vec=data[1]
        sum=data[2]
        with open(file,'w') as writer:
            writer.write(str(n)+"\n")
            writer.write(str(vec[0]))
            i=1
            while i<len(vec):
                writer.write(","+str(vec[i]))
                i+=1
            writer.write("\n"+str(sum))
