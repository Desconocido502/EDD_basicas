from Nodo import Nodo


class ListaDoblementeEnlazada():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def estaVacio(self):
        return self.primero == None
    
    def tamanio(self):
        return self.size

    def agregarAlInicio(self, dato):
        if self.estaVacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.size += 1

    def agregarAlFinal(self, dato):
        if self.estaVacio():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
    
    def eliminarAlInicio(self):
        if self.estaVacio():
            print("Lista vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1
    
    def eliminarAlFinal(self):
        if self.estaVacio():
            print("Lista vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1

    def recorrerLista(self): 
        if self.estaVacio(): 
            print("La lista esta vacía\n") 
        aux = self.primero 
        print(end='| ')
        while aux != None: 
            print(aux.dato, end=' | ') 
            aux = aux.siguiente
        print("\n")
        
    def buscarDato(self, date):
        if self.primero is None:
            print("La lista no tiene elementos")
        aux = self.primero
        while aux is not None:
            if aux.dato == date:
                return (f"{date}, Dato encontrado")
            aux = aux.siguiente
        return (f"{date}, Dato no encontrado")

    def ordenamiento(self):
        actual = aux = None
        if not (self.estaVacio()):
            actual = self.primero
            while (actual.siguiente):
                aux = actual.siguiente
                while (aux):
                    if (aux.dato < actual.dato):
                        tmp = actual.dato
                        actual.dato = aux.dato
                        aux.dato = tmp
                    aux = aux.siguiente
                actual = actual.siguiente
        else:
            print("No hay elementos")


lista = ListaDoblementeEnlazada()
lista.agregarAlInicio(10)
lista.agregarAlInicio(15)
lista.agregarAlInicio(77)
lista.agregarAlInicio(84)
lista.agregarAlFinal(95)
lista.agregarAlFinal(14)
lista.agregarAlFinal(82)
lista.agregarAlFinal(64)
lista.agregarAlInicio(78)
lista.recorrerLista()
lista.ordenamiento()
lista.recorrerLista()

print(lista.buscarDato(64))