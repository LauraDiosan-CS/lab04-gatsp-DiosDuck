from Service import Service
class UI():
    def __init__(self):
        self.__service=None
    def main(self):
        while 1:
            try:
                x = input()
                if x == "0":
                    return
                elif x == "1":
                    file=input()
                    self.__service=Service(file,1)
                    self.__service.prob1()
                    print("Functie terminata")
                elif x == "2":
                    file=input()
                    self.__service=Service(file,2)
                    self.__service.prob1()
                    print("Functie terminata")
                else:
                    print("Error")
            except FileNotFoundError:
                print("Fisierul nu exista")