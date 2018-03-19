import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';


import {AppComponent} from './app.component';
import {AuthModule} from "./auth/auth.module";
import {AppRouterModule} from "./app-router/app-router.module";
import {CommonModule} from "@angular/common";
import {HttpClientModule} from "@angular/common/http";
import {AlertModule} from "./alert/alert.module";
import {DashboardModule} from "./dashboard/dashboard.module";
import {NgbModule} from "@ng-bootstrap/ng-bootstrap";
import {CookieService} from "ngx-cookie-service";


@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    HttpClientModule,
    AuthModule,
    AlertModule,
    DashboardModule,
    AppRouterModule,
    NgbModule.forRoot()


  ],
  declarations: [
    AppComponent
  ],

  providers: [
    CookieService
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule {

}
