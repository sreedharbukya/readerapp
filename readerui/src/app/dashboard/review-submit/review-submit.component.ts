import {Component, EventEmitter, Input, OnInit, Output} from "@angular/core";
import {DashboardService} from "../dashboard.service";
import {AlertService} from "../../alert/alert.service";

@Component({
  selector: 'review-submit',
  templateUrl: 'review.submit.component.html'
})
export class ReviewSubmitComponent implements OnInit {
  @Input()
  public book;

  @Input()
  public reviewForm;


  @Output()
   public formSubmitted = new EventEmitter<boolean>();




  ngOnInit() {

  }

  public createReview(data: any) {
    this.formSubmitted.emit(data);
    this.reviewForm.reset();
  }


}
