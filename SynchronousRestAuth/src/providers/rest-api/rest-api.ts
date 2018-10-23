import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';

/*
  Generated class for the RestApiProvider provider.

  See https://angular.io/guide/dependency-injection for more info on providers
  and Angular DI.
*/
const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

@Injectable()
export class RestApiProvider {

  apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {
    console.log('Hello RestApiProvider Provider');
  }

  getSubjects() {
    return new Promise(resolve => {
      this.http.get(this.apiUrl+'/api/subjects').subscribe(data => {
        resolve(data);
      }, err => {
        console.log(err);
      });
    });
  }

  getSubjectById(id: string) {
    return this.http.get(this.apiUrl + '/api/subjects/' + id);
  }

  removeSubject(id: string) {
    return this.http.delete(this.apiUrl + '/api/subjects/' + id);
  }

  saveSubject(subject: any): Observable<any> {
    let result: Observable<Object>;
    if (subject['href']) {
      result = this.http.put(subject.href, subject);
    } else {
      result = this.http.post(this.apiUrl + '/api/subjects/', subject);
    }
    return result;
  }

  getActivities() {
    return new Promise(resolve => {
      this.http.get(this.apiUrl+'/api/activities').subscribe(data => {
        resolve(data);
      }, err => {
        console.log(err);
      });
    });
  }

  getActivityById(id: string) {
    return this.http.get(this.apiUrl + '/api/activities/' + id);
  }
}
