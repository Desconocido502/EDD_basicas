class NodoCelda(): # Nodos ortogonales
    def __init__(self, x, y, caracter):# 'caracter' puede ser cualquier valor
        self.caracter = caracter
        self.coordenadaX = x  # fila
        self.coordenadaY = y  # columna
        self.arriba = None
        self.abajo = None
        self.derecha = None  # self.siguiente
        self.izquierda = None  # self.anterior

    def setArriba(self, arriba):
        self.arriba = arriba
    

    def getArriba(self):
        return self.arriba
    

    def setAbajo(self, abajo):
        self.abajo = abajo
    

    def getAbajo(self):
        return self.abajo


    def setDerecha(self, derecha):
        self.derecha = derecha
    

    def getDerecha(self):
        return self.derecha
    

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda
    

    def getIzquierda(self):
        return self.izquierda