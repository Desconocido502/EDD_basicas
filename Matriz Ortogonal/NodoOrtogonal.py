class NodoOrtogonal():
    def __init__(self, fila, columna, caracter):
        self.fila = fila
        self.columna = columna
        self.caracter = caracter
        self.anterior = None
        self.siguiente = None
        self.arriba = None
        self.abajo = None
    
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna
    
    def getCaracter(self):
        return self.caracter
    
    def setArriba(self, arriba):
        self.arriba = arriba

    def getArriba(self):
        return self.arriba
    
    def setAbajo(self, abajo):
        self.abajo = abajo
    
    def getAbajo(self):
        return self.abajo
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente
    
    def getSiguiente(self):
        return self.siguiente
    
    def setAnterior(self, anterior):
        self.anterior = anterior
    
    def getAnterior(self):
        return self.anterior