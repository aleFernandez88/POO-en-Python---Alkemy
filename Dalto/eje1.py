class Estudiantes:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
            print(f'El estudiante {self.nombre} esta estudiado.')

nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Digame su grado: ")

Estudiante1 = Estudiantes(nombre,edad,grado)
    
estudiar = input()
if (estudiar.lower() == "estudiar"):
    Estudiante1.estudiar() 
       
    