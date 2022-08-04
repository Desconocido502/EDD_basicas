#include <iostream>
#include <String>
using namespace std;

#include "Nodo.h"

class DoublyCircularLinkedList{
	private:
		int tam;
		Nodo* primero;
		Nodo* ultimo;
	private:
		void __unirNodos();
	
	public:
		bool estaVacio();
		void insertarAlInicio(int, string, bool);
		void insertarAlFinal(int, string, bool);
		void eliminarAlInicio();
		void eliminarAlFinal();
		void desplegarListaIF(); 
		void desplegarListaFI(); 
		bool buscarNodo(int);
		bool actualizarNodo(int,string,bool);
		int tamanio();
		void sortLinkedList();
		DoublyCircularLinkedList();
};

DoublyCircularLinkedList::DoublyCircularLinkedList(){
	this->tam = 0;
	this->primero = NULL;
	this->ultimo = NULL;
}

//Metodo para saber si la lista esta vacia
bool DoublyCircularLinkedList::estaVacio(){
	return this->primero == NULL;
}

int DoublyCircularLinkedList::tamanio(){
	return this->tam;
}

void DoublyCircularLinkedList::__unirNodos(){
	if(this->primero != NULL){
		this->primero->anterior = this->ultimo;
		this->ultimo->siguiente = this->primero;
	}
}

void DoublyCircularLinkedList::insertarAlInicio(int edad, string nombre, bool estado){
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
	this->__unirNodos();
	this->tam += 1;
}

void DoublyCircularLinkedList::insertarAlFinal(int edad, string nombre, bool estado){
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
	this->__unirNodos();
	this->tam += 1;
}

bool DoublyCircularLinkedList::buscarNodo(int edad){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return false;
	}
	
	Nodo* aux = new Nodo();
	aux = this->primero;
	while(aux != NULL){
		if(aux->edad == edad){
			cout<<edad<<", encontrado"<<endl;
			return true;
		}
		aux = aux->siguiente;
		
		if(aux == this->primero){
			cout<<edad<<", no encontrado"<<endl;
			return false;
		}
	}
	cout<<"\n"<<endl;
}

bool DoublyCircularLinkedList::actualizarNodo(int edad, string nombre ,bool estado){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return false;
	}
	
	Nodo* aux = new Nodo();
	aux = this->primero;
	while(aux != NULL){
		
		if(aux->edad == edad){
			aux->nombre = nombre;
			aux->estado = estado;
			cout<<edad<<", actualizado. \n"<<endl;
			return true;
		}
		aux = aux->siguiente;
		
		if(aux == this->primero){
			cout<<edad<<", no encontrado para actualizar. \n"<<endl;
			return false;
		}
	}
	cout<<"\n"<<endl;

}

void DoublyCircularLinkedList::desplegarListaIF(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}
	
	Nodo* aux = new Nodo();
	aux = this->primero;
	while(aux != NULL){
		cout<<aux->edad<<","<<aux->nombre<<","<<aux->estado<< endl;
		aux = aux->siguiente;
		
		if(aux == this->primero){
			break;
		}
	}
	cout<<"\n"<<endl;
}

void DoublyCircularLinkedList::desplegarListaFI(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}
	
	Nodo* aux = new Nodo();
	aux = this->ultimo;
	while(aux != NULL){
		cout<<aux->edad<<","<<aux->nombre<<","<<aux->estado<< endl;
		aux = aux->anterior;
		
		if(aux == this->ultimo){
			break;
		}
	}
	cout<<"\n"<<endl;
}

void DoublyCircularLinkedList::eliminarAlInicio(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
	}else{
		this->primero = this->primero->siguiente;
	}
	this->__unirNodos();
}

void DoublyCircularLinkedList::eliminarAlFinal(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
	}else{
		this->ultimo = this->ultimo->anterior;
	}
	this->__unirNodos();
}

void DoublyCircularLinkedList::sortLinkedList(){
	Nodo* aux = new Nodo();
	Nodo* actual = new Nodo();
	Nodo* temp = new Nodo();
	
	if(!this->estaVacio()){
		actual = this->primero;
		while(actual->siguiente != this->primero){
			aux = actual->siguiente;
			while(aux != this->primero){
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

