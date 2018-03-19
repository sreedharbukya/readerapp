import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {AlertService} from "./alert.service";


@Component({
  selector: 'alert',
  templateUrl: 'alert.component.html'
})

export class AlertComponent implements OnDestroy, OnInit {
  private subscription: Subscription;
  message: any;

  constructor(private alertService: AlertService) {
    // subscribe to alert messages
  }


  ngOnInit(): void {
    this.subscription = this.alertService.getMessage().subscribe(message => {
      this.message = message;
    });

  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}
