from Nodo import Nodo

class ListaEnlazada():
    def __init__(self, node = None):
        self.node = node
    
    @property
    def is_empty(self):
        return self.node is None
    
    @property
    def head(self):
        if self.is_empty:
            raise Exception("No se pudo obtener el nodo cabeza, la lista esta vacia")
        else:
            return self.node.left
    
    @property
    def tail (self):
        if self.is_empty:
            raise Exception ("No se pudo obtener el nodo cola, la lista esta vacia")
        else:
            return self.node.right

    @property
    def length(self):
        if self.is_empty:
            return 0
        else:
            return 1 + self.tail.length
    
    def agregar_al_inicio(self,x):
        return ListaEnlazada(Nodo(x, self))
    
    def agregar_al_final(self,x):
        if self.is_empty:
            return self.agregar_al_inicio(x)
        else:
            return ListaEnlazada(Nodo(self.head, self.tail.agregar_al_final(x)))
    
    def eliminar_al_inicio(self):
        if self.is_empty:
            raise Exception("No se puede eliminar el nodo cabeza, la lista esta vacia")
        else:
            return self.tail
    
    def eliminar_al_final(self):
        if self.is_empty:
            raise Exception("No se puede eliminar el nodo cola, la lista esta vacia")
        elif self.tail.is_empty:
            return self.tail
        else:
            return ListaEnlazada(Nodo(self.head, self.tail.eliminar_al_final()))
    
    def numero_de_nodo(self, index = 0):
        if self.is_empty:
            raise Exception("Indice fuera de los limites")
        elif index == 0:
            return self.head
        else:
            return self.tail.numero_de_nodo(index-1)
    
    def __str__(self):
        if self.is_empty:
            return "None"
        else:
            return str(self.head) + " -> " + str(self.tail)
    
    @staticmethod
    def construir(x = None, *rest):
        if x is None:
            return ListaEnlazada()
        else:
            return ListaEnlazada(Nodo(x, ListaEnlazada.construir(*rest)))

lts = ListaEnlazada.construir(1,2,3,51)
print(lts)

print(lts.agregar_al_inicio(0))
print(lts.agregar_al_final(4))
print(lts.eliminar_al_inicio())
print(lts.eliminar_al_final())
print(lts.numero_de_nodo(2))