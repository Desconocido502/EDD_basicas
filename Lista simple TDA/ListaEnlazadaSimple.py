from Nodo import Nodo
from Persona import Persona

class listaEnlazadaSimple(): 
    def __init__(self): 
        self.primero = None 
        self.ultimo = None
    
    def estaVacio(self): 
        return self.primero == None
    
    def agregarAlInicio(self, dato): 
        if self.estaVacio(): 
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato) 
            aux.siguiente = self.primero
            self.primero = aux 

    def agregarAlFinal(self, dato): 
        if self.estaVacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = Nodo(dato)
            aux.siguiente = self.ultimo
    
    def eliminarAlInicio(self):
        if self.estaVacio():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
    
    def eliminarAlFinal(self):
        if self.estaVacio():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = None
    
    def recorrerLista(self): 
        if self.estaVacio():
            print("La lista esta vacia\n")
        aux = self.primero
        while aux != None:
            print(aux.dato)
            print("---------------------------------------------"*2,'\n')
            aux = aux.siguiente
        print("\n")
    
    def tamanio(self):
        count = 0 
        if self.estaVacio(): 
            return '0'
        aux = self.primero 
        while aux != None: 
            count += 1
            aux = aux.siguiente
        return count

    def ordenamientoPorEdad(self):
        actual = aux = None
        if not (self.estaVacio()):
            actual = self.primero
            while (actual.siguiente):
                aux = actual.siguiente
                while (aux):
                    if (aux.dato.getEdad() < actual.dato.getEdad()):
                        tmp = actual.dato
                        actual.dato = aux.dato
                        aux.dato = tmp
                    aux = aux.siguiente
                actual = actual.siguiente
        else:
            print("No hay elementos")
    
    def buscarporNombre(self, nombre):
        if self.primero is None:
            return ("La lista no tiene personas!!!")
        aux = self.primero
        while aux is not None:
            if aux.dato.getNombre() == nombre:
                return aux.dato
            aux = aux.siguiente
        return (f"{nombre}, persona no encontrada")


lista = listaEnlazadaSimple()
lista.agregarAlFinal(Persona('Carlos', 21, "8088545407000"))
lista.agregarAlInicio(Persona("Eduardo", 14, "4788740895150"))
lista.agregarAlInicio(Persona("Astrid", 45, "7845940513564"))
lista.agregarAlInicio(Persona("Pablo", 42, "487788454654545"))
lista.agregarAlInicio(Persona("Jose", 47, "45454541548478"))
lista.agregarAlInicio(Persona("Felipe", 27, "9849484846588"))
lista.agregarAlInicio(Persona("Maddison", 25, "470659895685"))
lista.agregarAlInicio(Persona("Maria", 36, "45418461789994"))
lista.agregarAlInicio(Persona("Rene", 40, "78641581324548"))
lista.agregarAlInicio(Persona("Nelson", 28, "45665484007480"))

print("Lista Sin ordenar")
lista.recorrerLista()
print("Lista ordenada por Edad")
lista.ordenamientoPorEdad()
lista.recorrerLista()

print(lista.buscarporNombre('Maria'))
print(lista.buscarporNombre('Aldair'))
lista.eliminarAlInicio()
lista.recorrerLista()
print(lista.tamanio())