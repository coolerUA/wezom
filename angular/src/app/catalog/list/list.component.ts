

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from './../../requests/requests.component';


@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.scss']
})
export class ListComponent implements OnInit {

  productList = {results: []};

  constructor(
    private http: HttpClient,
    private apiService: ApiService,
    private route: ActivatedRoute,
    ){

    this.route.params.subscribe(params => {
      if (params.hasOwnProperty('catId')) {
        this.getProductList({cat:params.catId});
      }
      else if (params.hasOwnProperty('SubCatId')) {
        this.getProductList({subcat:params.SubCatId});
      }
      else {
        this.getProductList({});
      }

    });

  }

  ngOnInit() {
  }

  getProductList(pars) {

      this.apiService.getProduclList(pars).subscribe((res: any) => {
        console.log(res)
        this.productList = res;
    });

 }

}
