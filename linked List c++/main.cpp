#include <iostream>
#include "LinkedList.h"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	LinkedList *lista = new LinkedList();
	lista->insertarAlInicio(22,"Carlos",false);
	lista->insertarAlInicio(32,"Kevin",true);
	lista->insertarAlInicio(14,"Jhon",false);
	lista->insertarAlInicio(15,"Luis",true);
	lista->insertarAlInicio(81,"Marinella",false);
	lista->insertarAlInicio(61,"Quinella",true);
	lista->insertarAlFinal(98,"Rony",false);
	lista->insertarAlFinal(16,"Sandra",true);
	lista->insertarAlFinal(47,"Paolina",true);
	lista->desplegarLista();
	
	lista->eliminarAlFinal();
	lista->eliminarAlInicio();
	
	lista->desplegarLista();
	
	lista->buscarNodo(16);
	lista->buscarNodo(-1);
	
	lista->actualizarNodo(98,"Roger", true);
	lista->desplegarLista();
	
	cout<<"El total de elementos en la lista es de: " << lista->tamanio() <<"\n"<<endl;
	
	lista->sortLinkedList();
	
	lista->desplegarLista();
	
	return 0;
}
