class Nodo {
  constructor(dato) {
    this.dato = dato;
    this.siguiente = null;
    this.anterior = null;
  }
}

class listaCircularDoble {
  constructor() {
    this.primero = null;
    this.ultimo = null;
  }

  estaVacia() {
    if (this.primero === null) {
      return true;
    } else {
      return false;
    }
  }

  unirNodos() {
    if (this.primero != null) {
      this.primero.anterior = this.ultimo;
      this.ultimo.siguiente = this.primero;
    }
  }

  agregarAlinicio(dato) {
    if (this.estaVacia()) {
      this.primero = this.ultimo = new Nodo(dato);
    } else {
      let auxiliar = new Nodo(dato);
      auxiliar.siguiente = this.primero;
      this.primero.anterior = auxiliar;
      this.primero = auxiliar;
    }
    this.unirNodos();
  }

  agregarAlfinal(dato) {
    if (this.estaVacia()) {
      this.primero = this.ultimo = new Nodo(dato);
    } else {
      let auxiliar = this.ultimo;
      this.ultimo = auxiliar.siguiente = new Nodo(dato);
      this.ultimo.anterior = auxiliar;
    }
    this.unirNodos();
  }

  eliminarAlinicio() {
    if (this.estaVacia()) {
      console.log("No se encontraron elementos");
    } else if (this.primero === this.ultimo) {
      this.primero = this.ultimo = null;
    } else {
      this.primero = this.primero.siguiente;
    }
    this.unirNodos();
  }

  eliminarAlfinal() {
    if (this.estaVacia()) {
      console.log("No se encontraron datos");
    } else if (this.primero === this.ultimo) {
      this.primero = this.ultimo = null;
    } else {
      this.ultimo = this.ultimo.anterior;
    }
    this.unirNodos();
  }

  buscar(_dato) {
    let auxiliar = this.primero;
    while (auxiliar) {
      if (auxiliar.dato.nombreCancion === _dato) {
        return auxiliar.dato + ", dato encontrado.";
      } else {
        auxiliar = auxiliar.siguiente;
        if (auxiliar === this.primero) return _dato + ", dato no encontrado";
      }
    }
  }

  recorrerIniocio_Fin() {
    let auxiliar = this.primero;
    while (auxiliar) {
      console.log(auxiliar.dato.toString());
      auxiliar = auxiliar.siguiente;
      if (auxiliar === this.primero) {
        break;
      }
    }
  }

  recorrerFin_Inicio() {
    let auxiliar = this.ultimo;
    while (auxiliar) {
      console.log(auxiliar.dato.toString());
      auxiliar = auxiliar.anterior;
      if (auxiliar === this.ultimo) {
        break;
      }
    }
  }

  recorrerDoble() {
    let auxiliar = this.primero,
      cont_aux = 0;
    while (auxiliar) {
      console.log(auxiliar.dato.toString());
      auxiliar = auxiliar.siguiente;
      if (auxiliar === this.primero) {
        cont_aux += 1;
        if (cont_aux === 2) break;
      }
    }
  }

  graficarDobleDot() {
    const MAXVALUE = 2;
    let aux = this.primero,
      cont = 0,
      cont_aux = 0,
      cadena = "";
    cadena += "digraph G { \n";
    cadena += "rankdir=LR \n";

    while (aux) {
      cadena += "Node" + String(cont) + '[label="' + aux.dato.tiempoCancion + '"];\n';
      cont += 1;
      aux = aux.siguiente;
      if (aux === this.primero){
        cont_aux += 1;
        if(cont_aux === MAXVALUE) break;
      }
    }
    cont = cont_aux = 0
    while (aux) {
        cadena += "Node" + String(cont) + " -> " + "Node" + String(cont + 1) + ";\n";
        cadena += "Node" + String(cont + 1) + " -> " + "Node" + String(cont) + ";\n";
      cont += 1;
      aux = aux.siguiente;
      if (aux === this.ultimo) {
        cont_aux += 1;
        if(cont_aux === MAXVALUE) break;
      }
    }
    cadena += "Node" + String(cont) + " -> " + "Node" + String(0) + ";\n"
    cadena += "Node" + String(0) + " -> " + "Node" + String(cont) + ";\n"
    cadena += "}";
    console.log(cadena);
    d3.select("#lienzo").graphviz().width(1350).height(500).renderDot(cadena);
  }

  graficarDOT() {
    let aux = this.primero;
    let cont = 0;
    let cadena = "";
    cadena += "digraph G { \n";
    cadena += "rankdir=LR \n";
    while (aux.siguiente != this.primero) {
      cadena +=
        "Node" + String(cont) + '[label="' + aux.dato.tiempoCancion + '"];\n';
      if (aux != this.primero) {
        cadena +=
          "Node" + String(cont - 1) + " -> " + "Node" + String(cont) + ";\n";
        cadena +=
          "Node" + String(cont) + " -> " + "Node" + String(cont - 1) + ";\n";
      }
      cont += 1;
      aux = aux.siguiente;
    }
    cadena +=
      "Node" + String(cont) + '[label="' + aux.dato.tiempoCancion + '"];\n';
    cadena +=
      "Node" + String(cont - 1) + " -> " + "Node" + String(cont) + ";\n";
    cadena +=
      "Node" + String(cont) + " -> " + "Node" + String(cont - 1) + ";\n";
    cadena += "Node" + String(cont) + " -> " + "Node" + String(0) + ";\n";
    cadena += "Node" + String(0) + " -> " + "Node" + String(cont) + ";\n";
    cadena += "}";
    console.log(cadena);
    d3.select("#lienzo").graphviz().width(900).height(500).renderDot(cadena);
  }

  ordenamientoBurbuja() {
    let auxiliar;
    let actual = (auxiliar = null);
    if (!this.estaVacia()) {
      actual = this.primero;
      while (actual.siguiente !== this.primero) {
        auxiliar = actual.siguiente;
        while (auxiliar !== this.primero) {
          if (auxiliar.dato.tiempoCancion < actual.dato.tiempoCancion) {
            let temporal = actual.dato;
            actual.dato = auxiliar.dato;
            auxiliar.dato = temporal;
          }
          auxiliar = auxiliar.siguiente;
        }
        actual = actual.siguiente;
      }
    } else {
      console.log("No se encontraron datos");
    }
  }
}

class Canciones {
  constructor(nombreCancion, tipoCancion, tiempoCancion) {
    this._nombreCancion = nombreCancion;
    this._tipoCancion = tipoCancion;
    this._tiempoCancion = tiempoCancion;
  }
  get nombreCancion() {
    return this._nombreCancion;
  }
  set nombreCancion(nombreCancion) {
    this._nombreCancion = nombreCancion;
  }
  get tipoCancion() {
    return this._tipoCancion;
  }
  set tipoCancion(tipoCancion) {
    this._tipoCancion = tipoCancion;
  }
  get tiempoCancion() {
    return this._tiempoCancion;
  }
  set tiempoCancion(tiempoCancion) {
    this._tiempoCancion = tiempoCancion;
  }

  toString() {
    return `Nombre: ${this._nombreCancion}, Tipo: ${this._tipoCancion}, Tiempo: ${this._tiempoCancion}`;
  }
}

console.log("Hola bb ");
let listaCanciones = new listaCircularDoble();
/*
listaCanciones.agregarAlinicio(new Canciones("Get Lucky", "Contemporanea", 4))
listaCanciones.agregarAlinicio(new Canciones("Starboy", "Regueton", 3))
listaCanciones.agregarAlinicio(new Canciones("Imagination", "Para fumar mota", 5))
listaCanciones.agregarAlinicio(new Canciones("Inside of my eyelids", "Para fumar mota", 2))
listaCanciones.agregarAlinicio(new Canciones("Wait a minute", "Tranquila", 3))
listaCanciones.agregarAlinicio(new Canciones("Notion", "Contemporanea", 2))
listaCanciones.agregarAlinicio(new Canciones("Instant crush", "Contemporanea", 5))
//listaCanciones.recorrerFin_Inicio()
console.log(listaCanciones.buscar("Starboy"))
listaCanciones.recorrerIniocio_Fin()*/

listaCanciones.agregarAlfinal(new Canciones("Get Lucky", "Contemporanea", 4));
listaCanciones.agregarAlfinal(new Canciones("Starboy", "Regueton", 3));
listaCanciones.agregarAlfinal(
  new Canciones("Imagination", "Para fumar mota", 5)
);
listaCanciones.agregarAlfinal(
  new Canciones("Inside of my eyelids", "Para fumar mota", 2)
);
listaCanciones.agregarAlfinal(new Canciones("Wait a minute", "Tranquila", 3));
listaCanciones.agregarAlfinal(new Canciones("Notion", "Contemporanea", 2));
listaCanciones.agregarAlfinal(
  new Canciones("Instant crush", "Contemporanea", 5)
);
//console.log(listaCanciones.buscar("Starboy"))
listaCanciones.ordenamientoBurbuja();
//listaCanciones.recorrerIniocio_Fin()
//listaCanciones.recorrerDoble();
listaCanciones.graficarDOT();
listaCanciones.graficarDobleDot();
//console.log(listaCanciones.primero.anterior.dato)
//console.log(listaCanciones.ultimo.siguiente.dato)
