import {Component, OnInit} from "@angular/core";
import {AlertService} from "../../alert/alert.service";
import {DashboardService} from "../dashboard.service";
import {Router} from "@angular/router";

@Component({
  selector: 'books-reviewed',
  templateUrl: 'book-reviewed.component.html'
})
export class BookReviewedComponent implements OnInit {

  public books: any[];
  public loading: boolean = true;


  constructor(private dashboardService: DashboardService,
              private alertService: AlertService,
              private router: Router) {

  }

  ngOnInit() {

    this.get_books_reviewed_by_me();

  }


  private get_books_reviewed_by_me() {
    this.dashboardService.get_books_reviewed().then(response => {
      console.log(response);
      this.books = response;
      this.loading = false;

    }).catch(error => {
      console.log(error);
      this.alertService.error("Error Occurred in fetching the books data!");
    })
  }

}
