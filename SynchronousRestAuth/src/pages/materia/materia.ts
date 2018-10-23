import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { User } from '../../providers';
import { RestApiProvider } from '../../providers/rest-api/rest-api'

/**
 * Generated class for the MateriaPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-materia',
  templateUrl: 'materia.html',
})
export class MateriaPage {

  subject = {
    name: ' ',
    credits: 0,
    teacher: ' ',
    grade: 0.0,
    description: ' '
  }

  constructor(public navCtrl: NavController,public user: User, public navParams: NavParams, public restProvider: RestApiProvider) {
  
  }
  account: { email: string, password: string } = {
    email: 'test@example.com',
    password: 'test'
  };

  ionViewDidLoad() {
    console.log('ionViewDidLoad MateriaPage');
  }
  saveSubject() {
    this.restProvider.saveSubject(this.subject).subscribe((result) => {
      console.log(result);
      this.navCtrl.push('PrincipalPage');
    }, (err) => {
      console.log(err);
    });
  }
  doLogout() {
    this.user.signup(this.account).subscribe((resp) => {
      this.navCtrl.push('LoginPage');
    }, (err) => {
      this.navCtrl.push('LoginPage');
    });
  }

}
