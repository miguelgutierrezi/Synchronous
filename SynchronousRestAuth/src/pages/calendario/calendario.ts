import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import { LoadingController } from 'ionic-angular';
@IonicPage()
@Component({
  selector: 'page-calendario',
  templateUrl: 'calendario.html',
})
export class CalendarioPage {

  

  constructor(public navCtrl: NavController, public navParams: NavParams,
    public loadingCtrl: LoadingController) {
  }

  ionViewDidLoad() {
    const loader = this.loadingCtrl.create({
        content: "EN ESTOS MOMENTOS NO ESTA DISPONIBLE",
        duration: 10000
      });
      this.navCtrl.push('PrincipalPage');
  }

  

}
