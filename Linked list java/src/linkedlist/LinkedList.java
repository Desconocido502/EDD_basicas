package linkedlist;

public class LinkedList {

    Nodo primero;
    Nodo ultimo;
    private int tam;

    public LinkedList() {
        this.primero = null;
        this.ultimo = null;
        this.tam = 0;
    }

    public boolean estaVacio() {
        return this.primero == null;
    }

    public int tamanio() {
        return this.tam;
    }

    public void insertarAlInicio(int edad, String nombre, boolean estado) {
        Nodo nuevo = new Nodo();
        Nodo aux = new Nodo();
        nuevo.setEdad(edad);
        nuevo.setNombre(nombre);
        nuevo.setEstado(estado);

        if (this.estaVacio()) {
            this.primero = this.ultimo = nuevo;
        } else {
            aux = nuevo;
            aux.siguiente = this.primero;
            this.primero = aux;
        }
        this.tam += 1;
    }

    public void insertarAlFinal(int edad, String nombre, boolean estado) {
        Nodo nuevo = new Nodo();
        Nodo aux = new Nodo();
        nuevo.setEdad(edad);
        nuevo.setNombre(nombre);
        nuevo.setEstado(estado);

        if (this.estaVacio()) {
            this.primero = this.ultimo = nuevo;
        } else {
            aux = this.ultimo;
            this.ultimo = nuevo;
            aux.siguiente = this.ultimo;
        }
        this.tam += 1;
    }

    public void eliminarAlInicio() {
        Nodo aux = new Nodo();

        if (this.estaVacio()) {
            System.out.println("La lista esta vacia");
            return;
        } else if (this.primero == this.ultimo) {
            this.primero = this.ultimo = null;
        } else {
            this.primero = this.primero.siguiente;
        }
    }

    public void eliminarAlFinal() {
        Nodo aux = new Nodo();

        if (this.estaVacio()) {
            System.out.println("La lista esta vacia");
            return;
        } else if (this.primero == this.ultimo) {
            this.primero = this.ultimo = null;
        } else {
            aux = this.primero;
            while (aux.siguiente != this.ultimo) {
                aux = aux.siguiente;
            }
            aux.siguiente = null;
        }

    }

    public boolean buscarNodo(int edad) {
        Nodo aux = new Nodo();

        if (this.estaVacio()) {
            System.out.println("La lista no contiene elementos... ");
            return false;
        }

        aux = this.primero;
        while (aux != null) {
            if (aux.getEdad() == edad) {
                System.out.println(String.valueOf(edad) + ", encontrado...\n");
                return true;
            }
            aux = aux.siguiente;
        }
        System.out.println(String.valueOf(edad) + ", no encontrado...\n");
        return false;
    }

    public boolean actualizarNodo(int edad, String nombre, boolean estado) {
        Nodo aux = new Nodo();

        if (this.estaVacio()) {
            System.out.println("La lista no contiene elementos... ");
            return false;
        }

        aux = this.primero;
        while (aux != null) {
            if (aux.getEdad() == edad) {
                aux.setNombre(nombre);
                aux.setEstado(estado);
                System.out.println(edad + ", actualizado...\n");
                return true;
            }
            aux = aux.siguiente;
        }
        System.out.println(String.valueOf(edad) + ", no encontrado para actualizar...\n");
        return false;
    }

    public void sortLinkedList() {
        Nodo actual = new Nodo();
        Nodo temp = new Nodo();
        Nodo aux = new Nodo();

        if (!this.estaVacio()) {
            actual = this.primero;
            while (actual.siguiente != null) {
                aux = actual.siguiente;
                while (aux != null) {
                    if (aux.getEdad() < actual.getEdad()) {
                        temp.setEdad(actual.getEdad());
                        temp.setNombre(actual.getNombre());
                        temp.setEstado(actual.isEstado());

                        actual.setEdad(aux.getEdad());
                        actual.setNombre(aux.getNombre());
                        actual.setEstado(aux.isEstado());

                        aux.setEdad(temp.getEdad());
                        aux.setNombre(temp.getNombre());
                        aux.setEstado(temp.isEstado());
                    }
                    aux = aux.siguiente;
                }
                actual = actual.siguiente;
            }

        } else {
            System.out.println("No hay elementos que ordenar en la lista...");
        }
    }

    public void insertionSort(Nodo headref) {
        Nodo sorted = null;
        Nodo current = this.primero;
        Nodo next = new Nodo();

        while (current != null) {

            //Almacena next para la siguiente iteracion
            next = current.siguiente;

            //inserta actual en la lista ordenada
            sortedInsert(current);

            //Actualizar actual
            current = next;

        }
        
        this.primero = sorted;

    }

    public void sortedInsert(Nodo newnode) {
        
    }

    public void desplegarLista() {
        if (this.estaVacio()) {
            System.out.println("La lista se encuentra vacia");
            return;
        }

        Nodo aux = new Nodo();
        aux = this.primero;
        while (aux != null) {
            System.out.println("Edad:" + String.valueOf(aux.getEdad()) + ", Nombre: " + aux.getNombre() + ", Estado: " + aux.isEstado());
            aux = aux.siguiente;
        }
    }

}
