class Nodo {
    constructor(_PersonajeMK) {
        this.PersonajeMK = _PersonajeMK
        this.siguiente = null
    }
}

class Listasimple{
    constructor() {
        this.cabecera = null
    }
    agregarPersonajes(_objetoPersonaje) {
        var tempo = new Nodo(_objetoPersonaje)
        tempo.siguiente = this.cabecera
        this.cabecera = tempo
    }

    mostrarPersonajesMarioKart() {
        var temporal = this.cabecera
        while (temporal != null) {
            console.log(temporal.PersonajeMK.nombre)
            console.log(temporal.PersonajeMK.puesto)
            console.log(temporal.PersonajeMK.velocidad)
            temporal = temporal.siguiente
        }
    }

    graficarlistaPersonajesMarioKart(){
        var codigodot = "digraph G {\nlabel=\" Mario kart \";\nnode [shape=box];\nrankdir=LR\n";
        var temporal = this.cabecera
        var conexiones ="";
        var nodos ="";
        var numnodo= 0;
        while (temporal != null) {
            nodos+=  "N" + numnodo + "[label=\"" + temporal.PersonajeMK.nombre + "\"];\n"
            if(temporal.siguiente != null){
                var auxnum = numnodo+1
                conexiones += "N" + numnodo + " -> N" + auxnum + ";\n"
            }
            temporal = temporal.siguiente
            numnodo++;            
        }
        codigodot += "//agregando nodos\n"
        codigodot += nodos+"\n"
        codigodot += "//agregando conexiones o flechas\n"
        codigodot += "\n"+conexiones+"\n}"
        console.log(codigodot)
        var arreglo = [0,2,3,4,5]
        d3.select("#lienzo").graphviz()
            .width(900)
            .height(500)
            .renderDot(codigodot)
    }
}

class Personaje{
    constructor(_nombre,_puesto,_velocidad){
        this.puesto = _puesto
        this.nombre = _nombre
        this.velocidad = _velocidad
    }
}

var listamarioKart = new Listasimple();
var personajemariokart = new Personaje("Mario","1ro","100KM")
listamarioKart.agregarPersonajes(personajemariokart)
personajemariokart = new Personaje("Yoshy","2ro","80KM")
listamarioKart.agregarPersonajes(personajemariokart)
personajemariokart = new Personaje("Bowser","3ro","750KM")
listamarioKart.agregarPersonajes(personajemariokart)
personajemariokart = new Personaje("Peach","4ro","50KM")
listamarioKart.agregarPersonajes(personajemariokart)

listamarioKart.mostrarPersonajesMarioKart()
listamarioKart.graficarlistaPersonajesMarioKart()