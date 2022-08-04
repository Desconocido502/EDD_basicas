#include <iostream>
#include <String>
using namespace std;

#include "Nodo.h"

class DoublyLinkedList{
	private:
		int tam;
		Nodo* primero;
		Nodo* ultimo;
	public:
		bool estaVacio();
		void insertarAlInicio(int, string, bool);
		void insertarAlFinal(int, string, bool);
		void eliminarAlInicio();
		void eliminarAlFinal();
		void desplegarLista(); 
		bool buscarNodo(int);
		bool actualizarNodo(int,string,bool);
		int tamanio();
		void sortLinkedList();
		DoublyLinkedList();
};

DoublyLinkedList::DoublyLinkedList(){
	this->tam = 0;
	this->primero = NULL;
	this->ultimo = NULL;
}

//Metodo para saber si la lista esta vacia
bool DoublyLinkedList::estaVacio(){
	return this->primero == NULL;
}

int DoublyLinkedList::tamanio(){
	return this->tam;
}

void DoublyLinkedList::insertarAlInicio(int edad, string nombre, bool estado){
	Nodo* nuevo = new Nodo();
	Nodo* aux = new Nodo();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
	}else{
		aux = nuevo;
		aux->siguiente = this->primero;
		this->primero->anterior = aux;
		this->primero = aux;
	}
	this->tam += 1;
}

void DoublyLinkedList::insertarAlFinal(int edad, string nombre, bool estado){
	Nodo* nuevo = new Nodo();
	Nodo* aux = new Nodo();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
	}else{
		aux = this->ultimo;
		this->ultimo = aux->siguiente = nuevo;
		this->ultimo->anterior = aux;
	}
	this->tam += 1;
}

void DoublyLinkedList::eliminarAlInicio(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}else if(this->primero->siguiente == NULL){
		this->primero = this->ultimo = NULL;
		this->tam = 0;
	}else{
		this->primero = this->primero->siguiente;
		this->primero->anterior = NULL;
		this->tam -= 1;
	}
}

void DoublyLinkedList::eliminarAlFinal(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}else if(this->primero->siguiente == NULL){
		this->primero = this->ultimo = NULL;
		this->tam = 0;
	}else{
		this->ultimo = this->ultimo->anterior;
		this->ultimo->siguiente = NULL;
		this->tam -= 1;
	}
}

bool DoublyLinkedList::buscarNodo(int edad){
	Nodo* aux = new Nodo();
	
	if(this->estaVacio()){
		cout<<"La lista no contiene elementos... "<<endl;
		return false;
	}
	
	aux = this->primero;
	while(aux != NULL){
		if(aux->edad == edad){
			cout<<edad<<" , encontrado. \n"<<endl;
			return true;
		}
		aux = aux->siguiente;
	}
	cout<<edad<<", no encontrado. \n"<<endl;
	return false;
}

bool DoublyLinkedList::actualizarNodo(int edad, string nombre, bool estado){
	Nodo* aux = new Nodo();
	
	if(this->estaVacio()){
		cout<<"La lista no contiene elementos... \n"<<endl;
		return false;
	}
	
	aux = this->primero;
	while(aux != NULL){
		if(aux->edad == edad){
			aux->nombre = nombre;
			aux->estado = estado;
			cout<<edad<<", actualizado. \n"<<endl;
			return true;
		}
		aux = aux->siguiente;
	}
	cout<<edad<<", no actualizado. \n"<<endl;
	return false;
}

void DoublyLinkedList::desplegarLista(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}
	Nodo* aux = new Nodo();
	aux = this->primero;
	while(aux != NULL){
		cout<<aux->edad<<","<<aux->nombre<<","<<aux->estado<< endl;
		aux = aux->siguiente;
	}
	cout<<"\n"<<endl;
}

void DoublyLinkedList::sortLinkedList(){
	Nodo* aux = new Nodo();
	Nodo* actual = new Nodo();
	Nodo* temp = new Nodo();
	
	if(!this->estaVacio()){
		actual = this->primero;
		while(actual->siguiente){
			aux = actual->siguiente;
			while(aux != NULL){
				if(aux->edad < actual->edad){
					temp->edad = actual->edad;
					temp->nombre = actual->nombre;
					temp->estado = actual->estado;
					
					actual->edad = aux->edad;
					actual->nombre = aux->nombre;
					actual->estado = aux->estado;
					
					aux->edad = temp->edad;
					aux->nombre = temp->nombre;
					aux->estado = temp->estado;
				}
				aux = aux->siguiente;
			}
			actual = actual->siguiente;
		}
	
		cout<<"Lista ordenada con exito!\n"<<endl;
	}else{
		cout<<"No hay elementos que ordenar"<<endl;
	}
	
}













