from Nodo import Nodo

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
            aux.siguienteNodo = None
    
    def recorrerLista(self): 
        if self.estaVacio(): 
            print("La lista esta vacía\n") 
        aux = self.primero
        print(end='\n| ')
        while aux != None: 
            print(aux.dato, end=' | ') 
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

lts_simple = listaEnlazadaSimple()
lts_simple.agregarAlInicio(10)
lts_simple.agregarAlInicio(15)
lts_simple.agregarAlInicio(77)
lts_simple.agregarAlInicio(84)
lts_simple.agregarAlFinal(95)
lts_simple.agregarAlFinal(14)
lts_simple.agregarAlFinal(82)
lts_simple.agregarAlFinal(64)
lts_simple.agregarAlInicio(78)
lts_simple.recorrerLista()
print(lts_simple.tamanio())