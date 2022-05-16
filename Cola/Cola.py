from Nodo import Nodo

class Cola():
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0
    
    def getTamanio(self):
        return self.tamanio
    
    def arribo(self, dato):
        #* Arriba el dato al final de la cola
        nodo_nuevo = Nodo(dato)
        if self.frente is None:
            self.frente = nodo_nuevo
        else:
            self.final.siguiente = nodo_nuevo
        self.final = nodo_nuevo
        self.tamanio += 1
    
    def atencion(self):
        #* Atiende el elemento en el frente de la cola y lo devuelve
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamanio -= 1
        return dato

    def esVacio(self):
        #* Devuelve true si la cola esta vacia
        return self.frente is None
    
    def en_frente(self):
        #* Devuelve el valor almacenado en el frente de la cola
        return str(self.frente.dato)
    
    def getTamanio(self):
        return self.tamanio
    
    def mover_al_final(self):
        #* Mueve el elemento del frente de la cola al final
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def listar(self):
        aux = self.frente
        if (self.esVacio()):
            return print("La cola esta vacia")
        self.temp = []
        while aux != None:
            self.temp.append(aux.dato)
            aux = aux.siguiente
        print(self.temp)
        
cola = Cola()
cola.arribo(15)
cola.arribo(20)
cola.arribo(25)
cola.arribo(30)
#*cola.mover_al_final()
cola.listar()
print(cola.getTamanio())
#print(cola.en_frente(), '---',cola.atencion())
cola.atencion()
cola.listar()
print(cola.getTamanio())