package linkedlist;

public class Nodo {

    private int edad;
    private String nombre;
    private boolean estado;
    Nodo siguiente;

    public Nodo() {
        this.edad = 0;
        this.nombre = "";
        this.estado = false;
        
        this.siguiente = null;
    }

    public Nodo(int edad, String nombre, boolean estado) {
        this.edad = edad;
        this.nombre = nombre;
        this.estado = estado;
        
        this.siguiente = null;
    }

    public int getEdad() {
        return edad;
    }

    public void setEdad(int edad) {
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public boolean isEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }
    
}
