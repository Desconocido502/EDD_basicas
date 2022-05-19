from NodoOrtogonal import NodoOrtogonal

class MatrizOrtogonal():
    def __init__(self):
        self.head = None
        self.size = 0 
        self.SizeG = 0
    
    def getHead(self):
        return self.head
    
    def getSize(self):
        return self.size
    
    def getSizeG(self):
        return self.SizeG

    def vacio(self):
        return self.head == None
    
    def autofilling(self, fila, columna, caracter):
        for i in range(1, fila + 1):
            for j in range(1, columna + 1):
                self.insertData(i, j, caracter)

    def insertData(self, fila, columna, caracter):
        self.SizeG += 1
        if self.vacio():
            new_node = NodoOrtogonal(fila, columna, caracter)
            self.head = new_node
            self.size += 1
        else:
            aux = self.head
            while aux.abajo != None:
                aux = aux.abajo
            if self.size != fila:
                self.size += 1
                new_node = NodoOrtogonal(fila, columna, caracter)
                aux.abajo = new_node
                new_node.arriba = aux
            else:
                while aux.siguiente != None:
                    aux = aux.siguiente
                new_node = NodoOrtogonal(fila, columna, caracter)
                aux.siguiente = new_node
                new_node.anterior = aux
                if self.size > 1:
                    aux2 = aux.arriba.siguiente
                    aux2.abajo = new_node
                    new_node.arriba = aux2

    def searchData(self, fila, columna):
        tmp = aux = None
        if (self.head != None):
            tmp = self.head
            while tmp != None:
                aux = tmp
                while aux != None:
                    if (int(fila) == int(aux.fila) and int(columna) == int(aux.columna)):
                        return aux.caracter #*Retorna el dato
                    aux = aux.siguiente
                tmp = tmp.abajo
            return None #*Devuelve nulo o vacio en caso de no encontrar el nodo con esas posiciones
        else:
            print("Matriz vacia")
            return 
    
    def printMatrixO(self):
        tmp = aux = None
        if (self.head != None):
            tmp = self.head
            while tmp != None:
                aux = tmp
                while aux != None:
                    print(aux.caracter + " ", end="")
                    aux = aux.siguiente
                print("")
                tmp = tmp.abajo
        else:
            return print("Matriz vacia")
        
fila = 6
columna = 9
Matriz = MatrizOrtogonal()

Matriz.autofilling(fila, columna, '*')
Matriz.printMatrixO()
# print(Matriz.getSizeG())
# print(Matriz.getSize())
# print(Matriz.searchData(4, 4))