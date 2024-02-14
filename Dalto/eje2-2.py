class Animal:
    def correr(self):
        print("Comeiendo")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando")
        
class Ave(Animal):
    def volar(self):
        print("Volando")
        
class Murcielago(Mamifero, Ave):
    pass
