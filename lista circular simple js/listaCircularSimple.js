class Canciones {
  constructor(nombreSong, tiempoSong, artistaSong, albumSong) {
    this._nombreSong = nombreSong;
    this._tiempoSong = tiempoSong;
    this._artistaSong = artistaSong;
    this._albumSong = albumSong;
  }
  get nombreSong() {
    return this._nombreSong;
  }
  set nombreSong(nombreSong) {
    this._nombreSong = nombreSong;
  }
  get tiempoSong() {
    return parseInt(this._tiempoSong);
  }
  set tiempoSong(tiempoSong) {
    this._tiempoSong = tiempoSong;
  }
  get artistaSong() {
    return this._artistaSong;
  }
  set artistaSong(artistaSong) {
    this._artistaSong = artistaSong;
  }
  get albumSong() {
    return this._artistaSong;
  }
  set albumSong(albumSong) {
    this._albumSong = albumSong;
  }

  toString() {
    return `Album: ${this._albumSong}, Cancion: ${this._nombreSong}, Artista: ${this._artistaSong}, Tiempo: ${this._tiempoSong}`;
  }
}

class Nodo {
  constructor(dato) {
    this.dato = dato;
    this.siguiente = null;
  }
}

class listaCircularSimple {
  constructor() {
    this.primero = null;
    this.ultimo = null;
  }

  estaVacia() {
    return this.primero === null;
  }

  agregarAlinicio(dato) {
    if (this.estaVacia()) {
      this.primero = this.ultimo = new Nodo(dato);
      this.ultimo.siguiente = this.primero;
    } else {
      let auxiliar = new Nodo(dato);
      auxiliar.siguiente = this.primero;
      this.primero = auxiliar;
      this.ultimo.siguiente = this.primero;
    }
  }

  agregarAlfinal(dato) {
    if (this.estaVacia()) {
      this.primero = this.ultimo = new Nodo(dato);
      this.ultimo.siguiente = this.primero;
    } else {
      let auxiliar = this.ultimo;
      this.ultimo = auxiliar.siguiente = new Nodo(dato);
      this.ultimo.siguiente = this.primero;
    }
  }

  eliminarAlinicio() {
    if (this.estaVacia()) {
      console.log("No se encontraron datos en la lista");
    } else if (this.primero === this.ultimo) {
      this.primero = this.ultimo = null;
    } else {
      this.primero = this.primero.siguiente;
      this.ultimo.siguiente = this.primero;
    }
  }

  eliminarAlfinal() {
    if (this.estaVacia()) {
      console.log("No se encontraron datos");
    } else if ((this.primero = this.ultimo)) {
      this.primero = this.ultimo = null;
    } else {
      let auxiliar = this.primero;
      while (auxiliar.siguiente != this.ultimo) {
        auxiliar = auxiliar.siguiente;
      }
      auxiliar.siguiente = this.primero;
      this.ultimo = auxiliar;
    }
  }

  recorrerLista() {
    if (this.estaVacia()) {
      console.log("No se encontraron datos");
    }
    let auxiliar = this.primero;
    while (auxiliar != null) {
      console.log(auxiliar.dato.toString());
      auxiliar = auxiliar.siguiente;
      if (auxiliar === this.primero) {
        break;
      }
    }
    console.log("\n");
  }

  buscarDato(dato_) {
    if (this.estaVacia()) {
      console.log("No se encontraron datos");
    }
    let auxiliar = this.primero;
    while (auxiliar != null) {
      if (auxiliar.dato.nombreSong === dato_) {
        return auxiliar.dato + ", dato encontrado.";
      }
      auxiliar = auxiliar.siguiente;
      if (auxiliar === this.primero) {
        return dato_ + ", dato no encontrado.";
      }
    }
  }

  tamanio() {
    let contador = 0;
    if (this.estaVacia()) {
      return 0;
    }
    let auxiliar = this.primero;
    while (auxiliar != null) {
      contador += 1;
      auxiliar = auxiliar.siguiente;
      if (auxiliar === this.primero) {
        console.log(contador);
      }
    }
  }

  ordenamientoBurbuja() {
    let auxiliar;
    let actual = (auxiliar = null);
    if (!this.estaVacia()) {
      actual = this.primero;
      while (actual.siguiente !== this.primero) {
        auxiliar = actual.siguiente;
        while (auxiliar !== this.primero) {
          if (auxiliar.dato.tiempoSong < actual.dato.tiempoSong) {
            let temporal = actual.dato;
            actual.dato = auxiliar.dato;
            auxiliar.dato = temporal;
          }
          auxiliar = auxiliar.siguiente;
        }
        actual = actual.siguiente;
      }
    } else {
      console.log("No se encontraron elementos");
    }
  }
}

console.log("Hola bb ");
let listaCanciones = new listaCircularSimple();

listaCanciones.agregarAlinicio(
  new Canciones("Desire", 4, "Years and Years", "Desconocido")
);
listaCanciones.agregarAlinicio(
  new Canciones("Fell me", 3, "Trueno", "Sencillo")
);
listaCanciones.agregarAlinicio(
  new Canciones("Algo me gusta de ti", 5, "Wisin & Yandel", "Desconocido")
);
listaCanciones.agregarAlinicio(new Canciones("Hurricane", 5, "Arty", "Remix"));
listaCanciones.agregarAlinicio(
  new Canciones("Ni contigo, ni sin ti", 2, "Pepe aguilar", "Esto si es cumbia")
);

console.log(listaCanciones.buscarDato("Hola"));

listaCanciones.recorrerLista();
listaCanciones.ordenamientoBurbuja();
listaCanciones.recorrerLista();
