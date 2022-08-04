#include <string>
#include <iostream>
using namespace std;

class NodoS{
	public:
		int edad;
		string nombre;
		bool estado;
		
		NodoS* siguiente;
		
	public:
		NodoS();
		NodoS(int edad, string nombre, bool estado);
};

NodoS::NodoS(){
	this->edad = 0;
	this->nombre = "";
	this->estado=false;
	
	this->siguiente = NULL;
}

NodoS::NodoS(int edad, string nombre, bool estado){
	this->edad = edad;
	this->nombre = nombre;
	this->estado = estado;
	
	this->siguiente = NULL;
}
