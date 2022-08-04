package linkedlist;

/**
 * @author CarlosSoto
 */
public class Principal {

    public static void main(String[] args) {
        LinkedList lista = new LinkedList();
        lista.insertarAlInicio(14, "Carlos", true);
        lista.insertarAlInicio(45, "Kevin", true);
        lista.insertarAlInicio(36, "Daniel", false);
        lista.insertarAlFinal(87, "Jonathan", true);
        lista.insertarAlFinal(24, "Yosef", false);
        lista.insertarAlFinal(36, "Ricardo", true);
        
        lista.desplegarLista();
        
        System.out.println("-------------------\n");
        
        lista.eliminarAlInicio();
        lista.eliminarAlFinal();
        lista.sortLinkedList();
        
        lista.desplegarLista();
        
        lista.buscarNodo(87);
        lista.buscarNodo(84);
        lista.actualizarNodo(87, "Rolando", false);
        
        lista.desplegarLista();
        
        
        System.out.println("El total de nodos en la lista es: " + String.valueOf(lista.tamanio()));
        
    }
    
}
