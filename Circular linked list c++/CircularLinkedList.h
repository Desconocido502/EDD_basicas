#include <iostream>
#include <String>
using namespace std;

#include "Nodo.h"

class CircularLinkedList{
	private:
		int tam;
		Nodo* primero;
		Nodo* ultimo;
	public:
		bool estaVacio();
		int tamanio();
		void insertarAlInicio(int, string, bool);
		void insertarAlFinal(int, string, bool);
		void eliminarAlInicio();
		void eliminarAlFinal();
		void desplegarLista(); 
		bool buscarNodo(int);
		bool actualizarNodo(int,string, bool);
		void sortLinkedList();
		CircularLinkedList();
};

CircularLinkedList::CircularLinkedList(){
	this->primero = NULL;
	this->ultimo = NULL;
	this->tam = 0;
}

bool CircularLinkedList::estaVacio(){
	return this->primero == NULL;
}

int CircularLinkedList::tamanio(){
	return this->tam;
}

void CircularLinkedList::insertarAlInicio(int edad, string nombre, bool estado){
	Nodo* nuevo = new Nodo();
	Nodo* aux = new Nodo();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
		this->ultimo->siguiente = this->primero;
	}else{
		aux = nuevo;
		aux->siguiente = this->primero;
		this->primero = aux;
		this->ultimo->siguiente = this->primero;
	}
	this->tam += 1;
}

void CircularLinkedList::insertarAlFinal(int edad, string nombre, bool estado){
	Nodo* nuevo = new Nodo();
	Nodo* aux = new Nodo();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
		this->ultimo->siguiente = this->primero;
	}else{
		aux = this->ultimo;
		this->ultimo = aux->siguiente = nuevo;
		this->ultimo->siguiente = this->primero;
	}
	this->tam += 1;
}

void CircularLinkedList::eliminarAlInicio(){
	if(this->estaVacio()){
		cout<<"La lista esta vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
		this->tam = 0;
	}else{
		this->primero = this->primero->siguiente;
		this->ultimo->siguiente = this->primero;
		this->tam -= 1;
	}
}

void CircularLinkedList::eliminarAlFinal(){
	
	if(this->estaVacio()){
		cout<<"La lista esta vaciaX"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
		this->tam = 0;
	}else {
		Nodo* aux = new Nodo();
		aux = this->primero;
		
		while(aux->siguiente != this->ultimo){
			aux = aux->siguiente;
		}
		aux->siguiente = this->primero;
		this->ultimo = aux;
		
		this->tam -= 1;
	}
}

bool CircularLinkedList::buscarNodo(int edad){
	if(this->estaVacio()){
		cout<<"La lista se encuentra vacia... \n"<<endl;
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
	return false;
}

bool CircularLinkedList::actualizarNodo(int edad, string nombre, bool estado){
	if(this->estaVacio()){
		cout<<"La lista se encuentra vacia... \n"<<endl;
		return false;
	}
	
	Nodo* aux = new Nodo();
	aux = this->primero;
	
	while(aux != NULL){
		
		if(aux->edad == edad){
			aux->nombre = nombre;
			aux->estado = estado;
			cout<<edad<<" , actualizado. \n"<<endl;
			return true;
		}
		
		aux = aux->siguiente;
		
		if(aux == this->primero){
			cout<<edad<<", no encontrado"<<endl;
			return false;
		}
	}
	return false;
}

void CircularLinkedList::desplegarLista(){
	if(this->estaVacio()){
		cout<<"La lista se encuentra vacia... \n"<<endl;
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

void CircularLinkedList::sortLinkedList(){
	Nodo* actual = new Nodo();
	Nodo* temp = new Nodo();
	Nodo* aux = new Nodo();
	
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
	}else{
		cout<<"No hay elementos que ordenar"<<endl;
	}
}




