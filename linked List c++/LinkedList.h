#include <iostream>
#include <String>
using namespace std;

#include "NodoS.h"

class LinkedList{
	private:
		NodoS* primero;
		NodoS* ultimo;
	public:
		bool estaVacio();
		void insertarAlInicio(int, string, bool);
		void insertarAlFinal(int, string, bool);
		void eliminarAlInicio();
		void eliminarAlFinal();
		void desplegarLista(); 
		bool buscarNodo(int);
		bool actualizarNodo(int,string, bool);
		int tamanio();
		void sortLinkedList();
		LinkedList();
};

LinkedList::LinkedList(){
	this->primero = NULL;
	this->ultimo = NULL;
}

//Metodo para saber si la lista esta vacia
bool LinkedList::estaVacio(){
	return this->primero == NULL;
}

int LinkedList::tamanio(){
	int count = 0;
	if(this->estaVacio()){
		return count;
	}
	NodoS* aux = new NodoS();
	aux = this->primero;
	while (aux != NULL){
		count += 1;
		aux = aux->siguiente;
	}
	return count;
}

//Metodos de ingreso de datos
void LinkedList::insertarAlInicio(int edad, string nombre, bool estado){
	NodoS* nuevo = new NodoS();
	NodoS* aux = new NodoS();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
	}else{
		aux = nuevo;
		aux->siguiente = this->primero;
		this->primero = aux;
	}
	
}

void LinkedList::insertarAlFinal(int edad, string nombre, bool estado){
	NodoS* nuevo = new NodoS();
	NodoS* aux = new NodoS();
	nuevo->edad = edad;
	nuevo->nombre = nombre;
	nuevo->estado = estado;
	
	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
	}else{
		aux = this->ultimo;
		this->ultimo = nuevo;
		aux->siguiente = this->ultimo;
	}
	
}

void LinkedList::eliminarAlInicio(){
	NodoS* aux = new NodoS();
	
	if(this->estaVacio()){
		cout<<"Lista vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
	}else{
		this->primero = this->primero->siguiente;
	}
}

void LinkedList::eliminarAlFinal(){
	NodoS* aux = new NodoS();
	
	if(this->estaVacio()){
		cout<<"Lista vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
	}else{
		aux = this->primero;
		while(aux->siguiente != this->ultimo){
			aux = aux->siguiente;
		}
		aux->siguiente = NULL;
	}
}

bool LinkedList::buscarNodo(int edad){
	NodoS* aux = new NodoS();
	
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

bool LinkedList::actualizarNodo(int edad, string nombre, bool estado){
	NodoS* aux = new NodoS();
	
	if(this->estaVacio()){
		cout<<"La lista no contiene elementos... \n"<<endl;
		return false;
	}
	
	aux = this->primero;
	while(aux != NULL){
		if(aux->edad == edad){
			aux->nombre = nombre;
			aux->estado = estado;
			cout<<edad<<" , actualizado. \n"<<endl;
			return true;
		}
		aux = aux->siguiente;
	}
	cout<<edad<<", no actualizado. \n"<<endl;
	return false;
}

void LinkedList::desplegarLista(){
	if(this->estaVacio()){
		cout<< "La lista se encuentra vacia"<<endl;
		return;
	}
	NodoS* aux = new NodoS();
	aux = this->primero;
	while(aux != NULL){
		cout<<aux->edad<<","<<aux->nombre<<","<<aux->estado<< endl;
		aux = aux->siguiente;
	}
	cout<<"\n"<<endl;
}


void LinkedList::sortLinkedList(){
	NodoS* actual = new NodoS();
	NodoS* temp = new NodoS();
	NodoS* aux = new NodoS();
	
	if(!this->estaVacio()){
		actual = this->primero;
		while(actual->siguiente != NULL){
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
	}else{
		cout<<"No hay elementos que ordenar"<<endl;
	}
}
