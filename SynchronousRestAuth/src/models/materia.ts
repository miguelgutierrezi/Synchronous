export class Materia {

    nombre;
    codigo;
    profesor;
    creditos;
    descripcion;
    starTime;
    endTime;
 
    constructor(public nom, public cod, public prof, public cred, public des, public star, public end){
        this.nombre = nom;
        this.codigo = cod;
        this.profesor = prof;
        this.creditos =cred;
        this.descripcion = des;
        this.starTime = star;
        this.endTime = end;
    }

 
}