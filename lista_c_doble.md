<h1>Lista Doblemente Enlazada</h1>

<p align="justify">Cada nodo (elemento) contiene dos enlaces, uno a su nodo predecesor y el otro a su nodo sucesor. La lista es eficiente tanto en recorrido directo (“adelante”) como en recorrido inverso (“atrás”).</p>

<p align="center"> 
<img src="./img/listaenlazadadoble.png" alt="lista doble"/> 
</p>

<p align="justify">La característica principal de una lista doble lineal es que los apuntadores del último nodo y del primer nodo apuntan hacia el valor nulo.</p>

<h4>Se presenta una lista de los métodos que usará la clase de Lista simple:</h4>

<ul>
    <li>Crear</li>
    <li>Recorrer Lista</li>
    <li>Tamaño</li>
    <li>Agregar
        <ul>
            <li>Agregar al Inicio</li>
            <li>Agregar al Final</li>
        </ul>
    </li>
    <li>Eliminar
        <ul>
            <li>Eliminar al Inicio</li>
            <li>Eliminar al Final</li>
        </ul>
    </li>
    <li>Esta vacio</li>
    <li>Buscar Dato</li>
</ul>

<h5>Para complementar la lista, necesitamos crear una clase nodo, la cual es la siguiente:</h5>

<h4>Clase NODO:</h4>

```python
class Nodo: 
    def __init__(self, dato): 
        self.dato = dato 
        self.siguiente = None
        self.anterior = None
```

<ul>
    <li>
    <p align="justify">Dato: Dato que contendrá el nodo, string, number, boolean, etc.</p> 
    </li>
    <li><p align="justify">Siguiente: Es el apuntador que contendrá la referencia en memoria del siguiente nodo.</p></li>
    <li><p align="justify">Anterior: Es el apuntador que contendrá la referencia en memoria del anterior nodo.</p></li>
</ul>

<h4>Clase Lista Enlazada Doble:</h4>

```python
from Nodo import Nodo

class ListaDoblementeEnlazada():
  def __init__(self):
    self.primero = None
    self.ultimo = None
    self.size = 0
    ......
```

h4>Métodos de la clase:</h5>

<h5>Esta vacio</h5>
<p align="justify">Método para saber si la lista se encuentra vacía, si esta vacío retorna True, en caso contrario False.</p>

```python
def estaVacio(self): 
    return self.primero == None
```

<h5>Agregar al inicio</h5>
<p align="justify">Inserta los nodos por la cabeza.</p>

```python
def agregarAlInicio(self): 
    if self.estaVacio():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = nodoLista(dato) 
      aux.siguiente = self.primero 
      self.primero.anterior = aux 
      self.primero = aux
    self.size += 1
```

<ul>
    <li>Si la lista esta vacia, tanto la cabeza como la cola apuntaran al nuevo nodo asignado.</li>
    <li>Sino, se agrega el nodo al inicio de la lista, osea al nodo cabeza.</li>
</ul>

<p align="justify">Se asigna el nuevo nodo a aux</p>

```python
aux = Nodo(dato)
```

<p align="justify">Ahora al apuntador siguiente de aux se le dice que almacene la referencia del nodo cabeza.</p>

```python
aux.siguiente = self.primero
```

<p align="justify">Bien, aqui le decimos a la cabeza que en su apuntador anterior almacene la referencia del nodo aux.</p>

```python
self.primero.anterior = aux
```

<p align="justify">Por último, Se le asigna al nodo cabeza, el valor que tiene aux, osea el nuevo nodo, convirtiendose en la nueva cabeza.</p>

```python
self.primero = aux
```

<p align="justify">Como se podrán dar cuenta, en dicho método se le aumenta una variable llamada size osea tamaño en español, y es la encargada de llevar el conteo de nodos, de está manera se lleva un mejor control del conteo de nodos y de la eficiencia de la memoria.</p>

<h4>Demostración gráfica:</h4>
<p align="center"> <img src="./img/dobleagregaralinicio.gif" alt="agregar al inicio"/> </p>

<h5>Agregar al final</h5>
<p align="justify">Inserta los nodos por la cola.</p>

```python
def agregarAlFinal(self): 
    if self.estaVacio():
      self.primero = self.ultimo = Nodo(dato)
    else:
      aux = self.ultimo
      self.ultimo = aux.siguiente = Nodo(dato)
      self.ultimo.anterior = aux
    self.size += 1
```
0
<ul>
    <li>Si la lista esta vacia, tanto la cabeza como la cola apuntaran al nuevo nodo asignado.</li>
    <li>Sino, se agrega el nodo al final de la lista, osea al nodo cola.</li>
</ul>

<p align="justify">Se asigna a aux el nodo cola.</p>

```python
aux = self.ultimo
```

<p align="justify">Ahora al nodo cola y al apuntador siguiente de aux se les asigna el nuevo nodo.</p>

```python
self.ultimo = aux.siguiente = Nodo(dato)
```

<p align="justify">Por último, al apuntador anterior del nodo cola se le asigna el valor de aux.</p>

```python
self.ultimo.anterior = aux
```