
import {NgModule, OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';
import { ListComponent } from './list/list.component';

import { RouterModule, Routes } from '@angular/router';

import {MatButtonModule} from '@angular/material/button';
import {MatCardModule} from '@angular/material/card';
import { FlexLayoutModule } from '@angular/flex-layout';

import { ApiService } from './../requests/requests.component';

import { FormsModule } from '@angular/forms';

import {MatFormFieldModule} from '@angular/material/form-field';
// import {MatInputModule} from '@angular/material';
import {MatSelectModule} from '@angular/material/select';
import {MatDialogModule} from '@angular/material/dialog';


const routes: Routes = [

  { path: '', component: ListComponent},
  { path: 'catalog/:catId', component: ListComponent},

];

@NgModule({
  declarations: [ListComponent],
  imports: [
    CommonModule,
    RouterModule.forChild(routes),
    MatButtonModule,
    MatCardModule,
    FlexLayoutModule,
    FormsModule,

    MatFormFieldModule,
    MatSelectModule,
    MatDialogModule
  ],
  providers: [
    ApiService
  ],

})
export class CatalogModule implements OnInit {
  constructor() { }

  ngOnInit(): void {

  }
}
