export class Materia {

    nombre;
    descripcion;
    creditos;
    nota;
    profesor;
    starTime;
    endTime;
 
    constructor(public nom, public des, public cred, public grade, public prof, public star, public end){
        this.nombre = nom;
        this.descripcion = des;
        this.creditos =cred;
        this.nota = grade;
        this.profesor = prof;
        this.starTime = star;
        this.endTime = end;
    }

 
}