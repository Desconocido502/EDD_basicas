from Nodo import Nodo

class listaEnlazadaSimple(): 
    def __init__(self): 
        self.primero = None 
        self.ultimo = None
        
    def getHead(self):
        return self.primero
    
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
    
    def sortedMerge(self, a, b):
        result = None
        
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
        
        # pick either a or b and recur..
        if a.dato <= b.dato:
            result = a
            result.siguiente = self.sortedMerge(a.siguiente, b)
        else:
            result = b
            result.siguiente = self.sortedMerge(a, b.siguiente)
        return result

    def mergeSort(self, h):
        
        # Base case if head is None
        if h == None or h.siguiente == None:
            return h

        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.siguiente

        # set the next of middle node to None
        middle.siguiente = None

        # Apply mergeSort on left list
        left = self.mergeSort(h)
        
        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)

        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if (head == None):
            return head

        slow = head
        fast = head

        while (fast.siguiente != None and
                fast.siguiente.siguiente != None):
            slow = slow.siguiente
            fast = fast.siguiente.siguiente
        
        return slow
    
    def buscarDato(self, date):
        if self.primero is None:
            print("La lista no tiene elementos")
        aux = self.primero
        while aux is not None:
            if aux.dato == date:
                return (f"{date}, Dato encontrado")
            aux = aux.siguiente
        return (f"{date}, Dato no encontrado")

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
#print(lts_simple.tamanio())
#lts_simple.ordenamiento()
lts_simple = lts_simple.mergeSort(lts_simple.getHead())
print(lts_simple.dato)
#lts_simple.recorrerLista()
#print(lts_simple.buscarDato(95))