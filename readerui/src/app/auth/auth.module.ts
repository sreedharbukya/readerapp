import {NgModule} from "@angular/core";
import {LoginComponent} from "./login/login.component";
import {CommonModule} from "@angular/common";
import {SignupComponent} from "./signup/signup.component";
import {LogoutComponent} from "./logout/logout.component";
import {RouterModule} from "@angular/router";
import {PageNotFoundComponent} from "./page-not-found/page-not-found.component";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";
import {AuthService} from "./auth.service";
import {AlertModule} from "../alert/alert.module";

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    AlertModule
  ],
  exports: [],
  declarations: [
    LoginComponent,
    LogoutComponent,
    SignupComponent,
    PageNotFoundComponent
  ],
  providers : [
    AuthService
  ]
})
export class AuthModule {

}
