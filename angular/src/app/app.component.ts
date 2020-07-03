import { Component } from '@angular/core';
import { ApiService } from './requests/requests.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  categories = [];

  constructor(
    private apiService: ApiService,
    ) {

      this.apiService.getCategoryList().subscribe((res: any) => {
        console.log(res);
      this.categories = res.results;
    });


    }

}

