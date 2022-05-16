from Nodo import Nodo

class Pila():
    def __init__(self):
        self.cima = None
        self.tamanio = 0
    
    def getTamanio(self):
        return self.tamanio
    
    def esVacio(self):
        return self.cima == None
    
    def cima(self):
        if self.cima is not None:
            return self.cima.dato
        else:
            return None

    def apilar(self, dato):
        self.tamanio += 1
        nuevo_nodo = Nodo(dato)
        if (self.esVacio()):
            self.cima = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cima
            self.cima = nuevo_nodo

    def desapilar(self):
        nodo_a_retirar = None
        if (not self.esVacio()):
            nodo_a_retirar = self.cima
            self.cima = self.cima.siguiente
            self.tamanio -= 1
        return nodo_a_retirar
    
    def listar(self):
        aux = self.cima
        if (self.esVacio()):
            return print("La pila esta vacia")
        print("-----------------")
        while aux != None:
            print("|\t" + str(aux.dato) + "\t|")
            print("-----------------")
            aux = aux.siguiente

pila = Pila()
pila.apilar(10)
pila.apilar(84)
pila.apilar(25)
pila.apilar(16)
pila.apilar(67)
pila.apilar(98)

pila.listar()
pila.desapilar()
print("Desapilamos un valor:")
pila.listar()