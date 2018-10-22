import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { User } from '../../providers';
import { RestApiProvider } from '../../providers/rest-api/rest-api'
/**
 * Generated class for the ActividadesPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-actividades',
  templateUrl: 'actividades.html',
})
export class ActividadesPage {

  public actividades: Array<Object> = [];

  constructor(public navCtrl: NavController, public navParams: NavParams,public user: User, public restProvider: RestApiProvider) {
    this.getActivities();
  }

  account: { email: string, password: string } = {
    email: 'test@example.com',
    password: 'test'
  };

  ionViewDidLoad() {
    console.log('ionViewDidLoad ActividadesPage');
  }

  getActivities() {
    this.restProvider.getActivities()
    .then((data: Array<Object>) => {
      this.actividades = data;
      console.log(data);
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
