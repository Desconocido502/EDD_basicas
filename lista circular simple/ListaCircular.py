from Nodo import Nodo

class ListaCircularSimple():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def estaVacio(self):
        return self.primero == None

    def agregarAlInicio(self, dato):
        if self.estaVacio():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    def agregarAlFinal(self, dato):
        if self.estaVacio():
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.siguiente = self.primero

    def eliminarAlInicio(self):
        if self.estaVacio():
            print("Lista vacia!")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    def eliminarAlFinal(self):
        if self.estaVacio():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux

    def recorrido(self):
        if self.estaVacio():
            print("La lista esta vacía\n")
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
            if aux == self.primero:
                break
        print("\n")

    def buscarDato(self, dato):
        if self.estaVacio():
            return "La lista no tiene elementos"
        aux = self.primero
        while aux != None:
            if aux.dato == dato:
                return f"{dato}, Dato encontrado"
            aux = aux.siguiente
            if aux == self.primero:
                return f"{dato}, Dato no encontrado"

    def tamanio(self):
        count = 0
        if self.estaVacio():
            return '0'
        aux = self.primero
        while aux != None:
            count += 1
            aux = aux.siguiente
            if aux == self.primero:
                return count

lista = ListaCircularSimple()
lista.agregarAlFinal(10)
lista.agregarAlFinal(48)
lista.agregarAlFinal(74)
lista.agregarAlInicio(25)
lista.agregarAlInicio(38)

lista.recorrido()

print(lista.buscarDato(11))
print('Tamaño:',lista.tamanio())

lista.eliminarAlFinal()
lista.eliminarAlInicio()
lista.recorrido()