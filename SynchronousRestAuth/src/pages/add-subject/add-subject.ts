import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';
import { RestApiProvider } from '../../providers/rest-api/rest-api'

/**
 * Generated class for the AddSubjectPage page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-add-subject',
  templateUrl: 'add-subject.html',
})
export class AddSubjectPage {

  subject = {
    name: ' ',
    credits: 0,
    teacher: ' ',
    grade: 0.0,
    description: ' '
  }

  constructor(public navCtrl: NavController, public navParams: NavParams, public restProvider: RestApiProvider) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad AddSubjectPage');
  }

  /*saveSubject() {
    this.restProvider.saveSubject(this.subject).then((result) => {
      console.log(result);
    }, (err) => {
      console.log(err);
    });
  }*/

}
