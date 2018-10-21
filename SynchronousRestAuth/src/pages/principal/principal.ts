import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { User } from '../../providers';
import { LoadingController } from 'ionic-angular';

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
  constructor(public navCtrl: NavController,public user: User, public navParams: NavParams,public loadingCtrl: LoadingController) {
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

}
