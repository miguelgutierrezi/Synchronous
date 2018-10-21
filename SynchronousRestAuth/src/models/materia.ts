export class Materia {

    nombre;
    codigo;
    profesor;
    creditos;
    descripcion;
    starTime;
    endTime;
 
    constructor(public nombre:string, public codigo:number, public profesor:string, public creditos:number, public descripcion:string, public starTime:string, public endTime:string){
        this.nombre = nombre;
        this.codigo = codigo;
        this.profesor = profesor;
        this.creditos =creditos;
        this.descripcion = descripcion;
        this.starTime = starTime;
        this.endTime = endTime;
    }

 
}