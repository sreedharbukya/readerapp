import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";

@Injectable()
export class DashboardService {
  private api_endpoint: string;

  constructor(private http: HttpClient) {
    this.onInit();

  }

  private onInit() {
    this.api_endpoint = environment.api_endpoint;
  }

  public create_book(data: any): Promise<any> {
    return this.http.post(this.api_endpoint + 'api/book/', data).toPromise();
  }

  public get_books_created_by_others(): Promise<any> {
    return this.http.get(this.api_endpoint + 'api/book/').toPromise()
  }


  public get_books_created(): Promise<any> {
    return this.http.get(this.api_endpoint + 'api/book/?owned=True').toPromise();
  }

  public get_books_reviewed(): Promise<any> {

    return this.http.get(this.api_endpoint + 'api/book/?reviewed=True').toPromise()
  }

  public create_review_for_book(data: any, book_isbn: string): Promise<any> {
    return this.http.post(this.api_endpoint + 'api/review/' + book_isbn + "/", data).toPromise();
  }

  public get_book_reviews(isbn_number: string): Promise<any> {
    return this.http.get(this.api_endpoint + 'api/review/' + isbn_number + "/").toPromise();

  }


}
