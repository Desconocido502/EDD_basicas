#include <string>
#include <iostream>
using namespace std;

class Nodo{
	public:
		int edad;
		string nombre;
		bool estado;
		
		Nodo* siguiente;
		
	public:
		Nodo();
		Nodo(int edad, string nombre, bool estado);
};

Nodo::Nodo(){
	this->edad = 0;
	this->nombre = "";
	this->estado=false;
	
	this->siguiente = NULL;
}

Nodo::Nodo(int edad, string nombre, bool estado){
	this->edad = edad;
	this->nombre = nombre;
	this->estado = estado;
	
	this->siguiente = NULL;
}

