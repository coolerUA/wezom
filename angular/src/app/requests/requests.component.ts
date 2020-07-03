import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {environment} from './../../assets/env';

@Injectable({
  providedIn: 'root'
})


export class ApiService {
  constructor(private http: HttpClient) {
  }

  getProduclList(pars) {
    if (pars.hasOwnProperty('cat')) {
      return this.http.get(`${environment.backendUrl}v1/market/product_list?category=${pars.cat}`);
    }
    return this.http.get(`${environment.backendUrl}v1/market/product_list`);
  }

  getCategoryList() {

    return this.http.get(`${environment.backendUrl}v1/generic/category/`);
  }

}
