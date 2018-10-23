import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestApiProvider } from '../../providers/rest-api/rest-api';

/**
 * Generated class for the InfoMateriaPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-info-materia',
  templateUrl: 'info-materia.html',
})
export class InfoMateriaPage {

  objetoRecibido: any;

  constructor(public navCtrl: NavController, public navParams: NavParams,public restProvider: RestApiProvider) {
    this.objetoRecibido = navParams.data;

  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad InfoMateriaPage');
  }

  borrarSubject(){
    this.restProvider.deleteSubject(this.objetoRecibido.id);
    this.navCtrl.push('PrincipalPage');
  }

}
