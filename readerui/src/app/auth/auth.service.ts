import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../environments/environment";
import {CookieService} from "ngx-cookie-service";

@Injectable()
export class AuthService {
  private api_endpoint: string;


  constructor(private http: HttpClient,
              private cookieService: CookieService) {
    this.onInit();

  }

  public isAuthenticated() {
    return this.cookieService.check('auth');
  }


  private onInit() {
    this.api_endpoint = environment.api_endpoint
  }


  public login(data: any): Promise<any> {
    return this.http.post(this.api_endpoint + 'api/reader/login/', data).toPromise()
  }


  public signup(data: any): Promise<any> {
    return this.http.post(this.api_endpoint + 'api/reader/signup/', data).toPromise();
  }

}
