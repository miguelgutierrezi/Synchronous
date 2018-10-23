import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { User } from '../../providers';
import { LoadingController } from 'ionic-angular';
import { Materia } from '../../models/materia';
import { RestApiProvider } from '../../providers/rest-api/rest-api';

/**
 * Generated class for the PrincipalPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-principal',
  templateUrl: 'principal.html',
})
export class PrincipalPage {

  public materias: Array<Object> = [];
  public materia:Object;

    parametros = {
      nombre: "Hola",
      creditos:0,
      profesor:"",
      nota:0,
      descripcion:""
    };

  constructor(public navCtrl: NavController,public user: User, public navParams: NavParams,public loadingCtrl: LoadingController, public restProvider: RestApiProvider) {
    this.getSubjects();
  }
  
  account: { email: string, password: string } = {
    email: 'test@example.com',
    password: 'test'
  };

  ionViewDidLoad() {
    console.log('ionViewDidLoad PrincipalPage');
  }
  doLogout() {
    this.user.signup(this.account).subscribe((resp) => {
      this.navCtrl.push('LoginPage');
    }, (err) => {
      this.navCtrl.push('LoginPage');
    });
  }
  calendario(){
    const loader = this.loadingCtrl.create({
        content: "EN ESTOS MOMENTOS NO ESTA DISPONIBLE",
        duration: 10000
      });
  }

  getSubjects() {
    this.restProvider.getSubjects()
    .then((data: Array<Object>) => {
      this.materias = data;
      console.log(data);
    });
  }

  removeSubject(nombre:string,credito,profe,not,desc) {
    this.parametros.nombre = nombre;
    this.parametros.creditos = credito;
    this.parametros.profesor = profe;
    this.parametros.nota = not;
    this.parametros.descripcion = desc;
    this.navCtrl.push('InfoMateriaPage', this.parametros);
  }


}