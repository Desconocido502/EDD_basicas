#include <iostream>

#include "CircularLinkedList.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	CircularLinkedList* listaC = new CircularLinkedList();
	
	listaC->insertarAlInicio(22,"Carlos",true);
	listaC->insertarAlInicio(42,"Jose",false);
	listaC->insertarAlInicio(24,"Yosef",true);
	listaC->insertarAlFinal(16,"Miriam",true);
	listaC->insertarAlFinal(35,"Luisa",true);
	listaC->insertarAlFinal(49,"Rene",false);
	
	listaC->desplegarLista();
	
	listaC->eliminarAlInicio();
	listaC->eliminarAlFinal();
	
	listaC->desplegarLista();
	
	cout<<"El total de elementos en la lista es: "<<listaC->tamanio()<<endl;
	
	listaC->buscarNodo(16);
	listaC->buscarNodo(45);
	
	listaC->actualizarNodo(16,"Fernando", false);
	
	listaC->desplegarLista();
	
	listaC->sortLinkedList();
	
	listaC->desplegarLista();
	
	return 0;
}
