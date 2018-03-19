import {NgModule} from "@angular/core";
import {CommonModule} from "@angular/common";
import {DashboardComponent} from "./dashboard.component";
import {DashboardService} from "./dashboard.service";
import {AlertModule} from "../alert/alert.module";
import {FooterComponent} from "./footer/footer.component";
import {RouterModule} from "@angular/router";
import {NewBooksComponent} from "./new-books/new-books.component";
import {AddBookComponent} from "./add-book/add-book.component";
import {BookReviewedComponent} from "./book-reviewed/book-reviewed.component";
import {BooksAddedComponent} from "./books-added/books-added.component";
import {BrowserModule} from "@angular/platform-browser";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {BookRatingsComponent} from "./book-ratings/book-ratings.component";
import {NgbModule} from "@ng-bootstrap/ng-bootstrap";
import {ReviewSubmitComponent} from "./review-submit/review-submit.component";
import {DashboardGuardService} from "./dashboard.guard.service";

@NgModule({
  imports: [
    CommonModule,
    BrowserModule,
    AlertModule,
    FormsModule,
    ReactiveFormsModule,
    NgbModule,
    RouterModule.forChild([
      {
        path: 'dashboard',
        component: DashboardComponent,
        canActivate: [DashboardGuardService],
        children: [
          {
            path: '',
            redirectTo: 'add-book',
            pathMatch: 'prefix'
          },
          {
            path: 'add-book',
            component: AddBookComponent,
            canActivate: [DashboardGuardService],

          },
          {
            path: 'new-books',
            component: NewBooksComponent,
            canActivate: [DashboardGuardService],

          },
          {
            path: 'books-reviewed',
            component: BookReviewedComponent,
            canActivate: [DashboardGuardService],

          },
          {
            path: 'books-added',
            component: BooksAddedComponent,
            canActivate: [DashboardGuardService],

          },
          {
            path: 'book-rating/:id',
            component: BookRatingsComponent

          }
        ]
      }
    ])

  ],
  exports: [
    RouterModule
  ],
  declarations: [
    DashboardComponent,
    FooterComponent,
    NewBooksComponent,
    AddBookComponent,
    BookReviewedComponent,
    BooksAddedComponent,
    BookRatingsComponent,
    ReviewSubmitComponent
  ],
  providers: [
    DashboardService,
    DashboardGuardService
  ]
})
export class DashboardModule {

}
