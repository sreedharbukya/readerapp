import {NgModule} from "@angular/core";
import {RouterModule} from "@angular/router";
import {LoginComponent} from "../auth/login/login.component";
import {CommonModule} from "@angular/common";
import {PageNotFoundComponent} from "../auth/page-not-found/page-not-found.component";
import {SignupComponent} from "../auth/signup/signup.component";
import {DashboardComponent} from "../dashboard/dashboard.component";
import {LogoutComponent} from "../auth/logout/logout.component";

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(
      [
        {
          path: '',
          redirectTo: 'login',
          pathMatch: 'full'

        },
        {
          path: 'login',
          component: LoginComponent
        },
        {
          path: 'logout',
          component: LogoutComponent
        },

        {
          path: 'signup',
          component: SignupComponent
        },
        {
          path: '**',
          component: PageNotFoundComponent

        }
      ]
    )
  ],
  exports: [
    RouterModule
  ]
})
export class AppRouterModule {

}
