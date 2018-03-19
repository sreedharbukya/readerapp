import {Component, OnInit} from "@angular/core";
import {DashboardService} from "../dashboard.service";
import {AlertService} from "../../alert/alert.service";
import {Router} from "@angular/router";
import {FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'new-books',
  templateUrl: 'new-books.component.html'
})
export class NewBooksComponent implements OnInit {

  public books: any[];
  public loading: boolean = true;

  public formsMap: Map<string, FormGroup> = new Map<string, FormGroup>();


  constructor(private dashboardService: DashboardService,
              private alertService: AlertService,
              private router: Router,
              private formBuilder: FormBuilder) {

  }

  async ngOnInit() {

    await this.get_recent_books_added_others();


  }

  private createReviewForm() {
    return this.formBuilder.group({
      // 'rating': [1, [Validators.required, Validators.max(5), Validators.min(1)]],
      // 'comments': ['', [Validators.required]]
      rating: new FormControl('', Validators.required),
      comment: new FormControl('', Validators.required)
    })
  }


  async get_recent_books_added_others() {

    this.alertService.reset();
    this.dashboardService.get_books_created_by_others().then(response => {
      console.log(response);
      this.books = response;
      this.loading = false;
      if (this.books) {
        this.createForms(this.books);
      }

    }).catch(error => {
      console.log(error);
      this.alertService.error("Error Occurred in fetching the books data!");
    })
  }


  async createForms(books: any[]) {

    if (this.books.length > 0) {
      for (let book of books) {
        await this.formsMap.set(book.isbn_number, this.createReviewForm());
      }
    }
  }


  public createReview(data: any, book_isbn: string) {

    console.log("Review Submitted", data, book_isbn);

    this.dashboardService.create_review_for_book(data, book_isbn).then(response => {
      console.log(response);
      this.alertService.success("Successfully created review");
      this.get_recent_books_added_others();
    }).catch(error => {
      console.log(error)
      this.alertService.error("Failed to create Review")
    })


  }

}
