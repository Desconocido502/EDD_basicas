#include <iostream>
#include "DoublyLinkedList.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	DoublyLinkedList* listaD = new DoublyLinkedList();
	
	listaD->insertarAlInicio(21,"Carlos",false);
	listaD->insertarAlInicio(14,"Eduardo",true);
	listaD->insertarAlFinal(57,"Sofia",false);
	listaD->insertarAlFinal(24,"Ana",true);
	listaD->insertarAlFinal(45,"Jimena",false);
	listaD->insertarAlFinal(84,"Rafael",true);
	listaD->insertarAlFinal(61,"Pablo",true);
	
	listaD->desplegarLista();
	
	listaD->eliminarAlInicio();
	listaD->eliminarAlFinal();
	
	listaD->desplegarLista();
	
	listaD->buscarNodo(14);
	listaD->actualizarNodo(57,"Adriana",true);
	
	listaD->sortLinkedList();
	
	listaD->desplegarLista();
	cout<<"El total de elementos de la lista es: "<<listaD->tamanio()<<endl;
	
	return 0;
}
