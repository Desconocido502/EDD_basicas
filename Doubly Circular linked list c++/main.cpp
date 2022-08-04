#include <iostream>

#include "DoublyCircularLinkedList.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	DoublyCircularLinkedList* listaDC = new DoublyCircularLinkedList();
	
	listaDC->insertarAlInicio(22,"Carlos", false);
	listaDC->insertarAlInicio(29,"Dylan", false);
	listaDC->insertarAlInicio(41,"Joshua", true);
	listaDC->insertarAlFinal(98,"Natalia",false);
	listaDC->insertarAlInicio(36,"Neymar", false);
	listaDC->insertarAlFinal(47,"Lilia",true);
	
	
	listaDC->desplegarListaIF();
	cout<<"\n------------------\n"<<endl;
	listaDC->desplegarListaFI();
	
	listaDC->eliminarAlInicio();
	listaDC->eliminarAlFinal();
	
	cout<<"\n------------------\n"<<endl;
	listaDC->desplegarListaIF();
	
	listaDC->buscarNodo(29);
	listaDC->buscarNodo(15);
	
	listaDC->actualizarNodo(29,"Dorian",true);
	listaDC->desplegarListaIF();
	
	listaDC->sortLinkedList();
	cout<<"\n------------------\n"<<endl;
	listaDC->desplegarListaIF();
	
	return 0;
}
