<h1>Introducción a las listas enlazadas</h1>

<p align="justify">Una <strong>lista enlazada (linked list)</strong> es una colección o secuencia  de elementos dispuestos unos detrás de otro, en la que cada elemento se conecta al siguiente elemento por un <strong>enlace</strong> o <strong>referencia.</strong></p>

<p align="center"> 
<img src="./img/lineales.png" alt="edd"/> 
<figcaption align="center">Fig.2 - Ejemplo de lista enlazada</figcaption>
</p>

<h3>¿Qué es un nodo?</h3>
<p align="justify">Un nodo en una lista enlazada contiene el valor de los datos y el puntero que apunta a la ubicación del siguiente nodo en la lista enlazada. Osea está compuesto por dos partes: Un valor y un apuntador de la referencia del siguiente nodo.</p>

<p align="center"> 
<img src="./img/nodo.png" alt="edd" width="260"/> 
<figcaption align="center">Fig.3 - Ejemplo de un nodo</figcaption>
</p>

<h3>Tipos de listas enlazadas:</h3>
<p align="justify">Existen 4 implementaciones diferentes de Lista enlazada disponibles, son:</p>

<ul>
    <li>Lista enlazada simple (Singly Linked List)</li>
    <li>Lista enlazada doble (Doubly Linked List)</li>
    <li>Lista enlazada circular simple (Singly Circular Linked List)</li>
    <li>Lista enlazada circular doble (Doubly Circular Linked List)</li>
</ul>


<h4>Ventajas de listas enlazadas:</h4>
<ul>
    <li><p align="justify">Son de naturaleza dinámica que asigna la memoria cuando es necesario.</p></li>
    <li><p align="justify">Las operaciones de inserción y eliminación se pueden implementar fácilmente.</p></li>
    <li><p align="justify">Las pilas y las colas se pueden ejecutar fácilmente.</p></li>
    <li><p align="justify">Lista enlazada reduce el tiempo de acceso.</p></li>
</ul>

<h4>Desventajas de listas enlazadas:</h4>
<ul>
    <li><p align="justify">La memoria se desperdicia ya que los punteros requieren memoria adicional para el almacenamiento.</p></li>
    <li><p align="justify">No se puede acceder a ningún elemento aleatoriamente; tiene que acceder a cada nodo secuencialmente.</p></li>
    <li><p align="justify">El desplazamiento inverso es difícil en la lista enlazada.</p></li>
</ul>

<h4>Operaciones de listas enlazadas:</h4>
<ul>
    <li><strong>Recorrido:</strong>
    <p align="justify">Consiste en visitar todos los nodos que forman parte de una lista. Para recorrer todos los nodos de la lista se posiciona en el primer nodo de la lista y después avanzar hacia el nodo que apunte el enlace al  siguiente nodo y así sucesivamente hasta encontrar el fin de la lista.</p></li>
    <li><strong>Inserción:</strong>
    <p align="justify">Consiste en agregar un nuevo nodo a una lista. La ubicación del nuevo nodo puede ser al inicio, al final o en cualquier posición dentro de la lista.</p></li>
    <li><strong>Borrado:</strong>
    <p align="justify">Consiste en eliminar un nodo de la lista y redireccionar los enlaces de los nodos antecesor y sucesor. La eliminación del nodo puede ser al inicio, al final o en cualquier posición dentro de la lista.</p></li>
    <li><strong>Búsqueda:</strong>
    <p align="justify">Consiste en recorrer todos los nodos de la lista desde el primer nodo para ir comparando el valor de cada nodo con el valor que se está buscando hasta encontrar el nodo con el valor indicado o encontrar el fin de la lista.</p></li>
</ul>

<h3>Redireccionamiento a cada tipo de listas enlazadas a trabajar:</h3>
<ul>
    <li><a href="./lista_simple.md">Lista simplemente enlazada</a></li>
    <li><a href="./lista_doble.md">Lista doblemente enlazada</a></li>
    <li><a href="./lista_c_simple.md">Lista circular simplemente enlazada</a></li>
    <li><a href="./lista_c_doble.md">Lista circular doblemente enlazada</a></li>
</ul>