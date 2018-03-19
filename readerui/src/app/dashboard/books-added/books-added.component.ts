import {Component, OnInit} from "@angular/core";
import {AlertService} from "../../alert/alert.service";
import {DashboardService} from "../dashboard.service";

@Component({
  selector: 'books-added',
  templateUrl: 'books-added.component.html'
})
export class BooksAddedComponent implements OnInit {
  public books: any[];
  public loading: boolean = true;

  constructor(private alerService: AlertService,
              private dashboardService: DashboardService,) {

  }

  ngOnInit() {

    this.dashboardService.get_books_created().then(response => {
      let data = response;

      this.books = data;
      this.loading = false;
    }).catch(error => {
      console.log("Error Occurred ", error);
      this.alerService.error("Error Occurred in fetching Books");
      this.loading = false;
    })
  }

}
