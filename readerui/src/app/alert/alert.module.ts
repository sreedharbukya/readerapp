import {NgModule} from "@angular/core";
import {AlertService} from "./alert.service";
import {AlertComponent} from "./alert.componet";
import {CommonModule} from "@angular/common";

@NgModule({
  imports: [
    CommonModule,


  ],

  providers: [
    AlertService

  ],
  declarations: [
    AlertComponent
  ],
  exports: [
    AlertComponent
  ],
})
export class AlertModule {

}
