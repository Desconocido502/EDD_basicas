from NodoCabecera import NodoCabecera

class ListaCabecera():
    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None
        self.tipo = tipo #* Si son Columnas o Filas
        self.size = 0
    
    def getHead(self):
        return self.primero
    
    def isEmpty(self):
        return self.primero == None
    
    def insertar_nodoCabecera(self, nuevo : NodoCabecera):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # ---- Insercion en ORDEN
            # -- verificamos si el nuevo es menor que el primero
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # -- verificamos si el nuevo es mayor que el ultimo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                # -- sino, recorremos la lista para buscar donde acomodarnos, entre el primero y el ultimo
                tmp: Nodo_Cabecera = self.primero 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break
    
    def mostrarCabeceras(self):
        tmp = self.primero
        while tmp != None:
            print('Cabecera', self.tipo, tmp.id)
            tmp = tmp.siguiente
    
    def getCabecera(self, id): #esta funcion debe retornar un nodo cabecera
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None
    
# filas = ListaCabecera('Fila')
# n8 = NodoCabecera(8)
# n6 = NodoCabecera(6)
# n10 = NodoCabecera(10)
# n7 = NodoCabecera(7)
# filas.insertar_nodoCabecera(n7)
# filas.insertar_nodoCabecera(n10)
# filas.insertar_nodoCabecera(n6)
# filas.insertar_nodoCabecera(n8)
# filas.mostrarCabeceras()

# print(filas.getCabecera(8).id)