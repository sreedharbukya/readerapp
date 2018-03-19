import {Component, OnInit} from "@angular/core";
import {Router} from "@angular/router";
import {CookieService} from "ngx-cookie-service";

@Component({
  selector: 'logout',
  templateUrl: 'logout.component.html'
})
export class LogoutComponent implements OnInit {

  constructor(private router: Router,
              private cookieService: CookieService) {

  }


  ngOnInit() {
    this.clearCookies();

  }

  private clearCookies() {
      console.log(this.cookieService.get('auth'));
      console.log("Cookies cleared");
      this.cookieService.delete('auth');
  }

  public redirectToLogin() {

    this.router.navigate(['login'])

  }
}
