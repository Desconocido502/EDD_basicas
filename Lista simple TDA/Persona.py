class Persona():
    def __init__(self, nombre, edad, Id):
        self.nombre = nombre
        self.edad = edad
        self.Id = Id

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setId(self, Id):
        self.Id = Id

    def getId(self):
        return self.Id

    def __str__(self):
        return f"Hola mi nombre es: {self.nombre}, mi edad es: {self.edad}, y mi No. de Identificacion es: {self.Id}"

# persona1 = Persona("Carlos", 21, 3018554470101)
# print(persona1)