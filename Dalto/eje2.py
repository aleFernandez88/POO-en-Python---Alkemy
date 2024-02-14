class Persona:
    def __init__(self,Nombre,Apellido,Edad):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        
    def datosPersona(self):
        
        return(f"HOla tengo una sed y soy {self.Nombre}")
        
class Estudiante(Persona):
    def __init__(self,Nombre,Apellido,Edad,Grado):
        Persona.__init__(self,Nombre,Apellido,Edad)
        self.Grado = Grado
        
    def grado(self):
        return(self.Grado,self.Nombre,self.Apellido,self.Edad)
        
        
persona1 = Estudiante("ale","fer","24","4")
print(persona1.grado())
print(persona1.datosPersona())