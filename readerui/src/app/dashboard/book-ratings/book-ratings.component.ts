import {Component, OnDestroy, OnInit} from "@angular/core";
import {ActivatedRoute, Router} from "@angular/router";
import {AlertService} from "../../alert/alert.service";
import {DashboardService} from "../dashboard.service";
import {Subscription} from "rxjs/Subscription";

@Component({
  selector: 'book-rating',
  templateUrl: 'book-ratings.component.html'
})
export class BookRatingsComponent implements OnInit, OnDestroy {
  private routerSubscription: Subscription;
  public selectedBookId: string;

  public reviews: any[];
  public loading: boolean = true;


  constructor(private router: Router,
              private activatedRoute: ActivatedRoute,
              private alertService: AlertService,
              private dashboardService: DashboardService) {
  }

  ngOnInit(): void {

    this.routerSubscription = this.activatedRoute.params.subscribe(params => {
      console.log("Id ", params);

      this.selectedBookId = params['id'];

      if (this.selectedBookId) {
        this.get_reviews(this.selectedBookId);
      }
    })

  }

  private get_reviews(book_isbn: string) {

    this.dashboardService.get_book_reviews(book_isbn).then(response => {
      console.log(response);
      this.reviews = response;
      this.loading = false;
    }).catch(error => {
      console.log("error", error);
      this.alertService.error("Failed to get reviews");
    })

  }

  ngOnDestroy(): void {
    this.routerSubscription.unsubscribe();
  }


}
