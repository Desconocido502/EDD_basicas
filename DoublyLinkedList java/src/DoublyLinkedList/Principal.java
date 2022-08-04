package DoublyLinkedList;

/**
 *
 * @author CarlosSoto
 */
public class Principal {

    public static void main(String[] args) {
        DoublyLinkedList listaD =  new DoublyLinkedList();
        listaD.insertarAlInicio(21, "Carlos", true);
        listaD.insertarAlInicio(14, "Kevin", false);
        listaD.insertarAlInicio(45, "Rolando", true);
        listaD.insertarAlInicio(36, "Samuel", false);
        listaD.insertarAlFinal(10, "Karla", false);
        listaD.insertarAlFinal(25, "Sofia", true);
        listaD.insertarAlFinal(35, "Duki", true);
        
        listaD.desplegarLista();
        
    }
}
