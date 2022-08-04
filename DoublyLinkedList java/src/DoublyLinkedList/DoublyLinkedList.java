package DoublyLinkedList;

/**
 *
 * @author CarlosSoto
 */
public class DoublyLinkedList {
    
    private int tam;
    Nodo primero;
    Nodo ultimo;
    
    public DoublyLinkedList(){
        this.tam = 0;
        this.primero = null;
        this.ultimo = null;
    }
    
    public boolean estaVacio(){
        return this.primero == null;
    }
    
    public int tamanio(){
        return this.tam;
    }
    
    public void insertarAlInicio(int edad, String nombre, boolean estado){
        Nodo nuevo = new Nodo();
        Nodo aux = new Nodo();
        
        nuevo.setEdad(edad);
        nuevo.setNombre(nombre);
        nuevo.setEstado(estado);
        
        if(this.estaVacio()){
            this.primero = this.ultimo = nuevo;
        }else{
            aux = nuevo;
            aux.siguiente = this.primero;
            this.primero.anterior = aux;
            this.primero = aux;
        }
        this.tam += 1;
    }
    
    public void insertarAlFinal(int edad, String nombre, boolean estado){
        Nodo nuevo = new Nodo();
        Nodo aux = new Nodo();
        
        nuevo.setEdad(edad);
        nuevo.setNombre(nombre);
        nuevo.setEstado(estado);
        
        if(this.estaVacio()){
            this.primero = this.ultimo = nuevo;
        }else{
            aux = this.ultimo;
            this.ultimo = aux.siguiente = nuevo;
            this.ultimo.anterior = aux;
        }
        this.tam += 1;
    }
    
    public void eliminarAlInicio(){
        if(this.estaVacio()){
            System.out.println("La lista esta vacia..");
            return;
        }else if(this.primero.siguiente == null){
            this.primero = this.primero.siguiente;
            this.primero.anterior = null;
            this.tam =0;
        }else{
            this.primero = this.primero.siguiente;
            this.primero.anterior = null;
            this.tam -= 1;
        }
    }
    
    public void eliminarAlFinal(){
        if(this.estaVacio()){
            System.out.println("La lista esta vacio...");
            return;
        }else if(this.primero.siguiente == null){
            this.primero = this.ultimo = null;
            this.tam = 0;
        }else{
            this.ultimo = this.ultimo.anterior;
            this.ultimo.siguiente = null;
            this.tam -= 1;
        }
    }
    
    public boolean buscarNodo(int edad){
        Nodo aux = new Nodo();
        
        if(this.estaVacio()){
            System.out.println("La lista no contiene alementos...");
            return false;
        }
        
        aux = this.primero;
        while(aux != null){
            if(aux.getEdad() == edad){
                System.out.println(String.valueOf(edad) + ", encontrado...\n");
                return true;
            }
            aux = aux.siguiente;
        }
        System.out.println(String.valueOf(edad) + ", no encontrado.\n");
        return false;
    }
    
    public boolean actualizarNodo(int edad, String nombre, boolean estado){
        Nodo aux = new Nodo();
        
        if(this.estaVacio()){
            System.out.println("La lista no contiene elementos...");
            return false;
        }
        
        aux = this.primero;
        while(aux != null){
            if(aux.getEdad() == edad){
                aux.setNombre(nombre);
                aux.setEstado(estado);
                System.out.println(String.valueOf(edad)+", actualizado. \n");
                return true;
            }
            aux = aux.siguiente;
        }
        System.out.println(String.valueOf(edad)+", no actualizado... \n");
        return false;
    }
    
    public void desplegarLista(){
        if(this.estaVacio()){
            System.out.println("La lista esta vacia");
            return;
        }
        
        Nodo aux = new Nodo();
        aux = this.primero;
        while(aux != null){
            System.out.println("Edad: "+String.valueOf(aux.getEdad()) + ", nombre: " + aux.getNombre() + ", Estado: "+aux.isEstado());
            aux = aux.siguiente;
        }
        System.out.println("");
        
    }
}
