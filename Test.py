class Pierwsza():
    def dodaj(self):
        a = 1
        return a

class Druga(Pierwsza):
    def sumuj(self):
        print(self.dodaj() + 10)

def main ():
    druga = Druga.sumuj(Pierwsza)

main()