import {Injectable} from "@angular/core";
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot} from "@angular/router";
import {CookieService} from "ngx-cookie-service";
import {Observable} from "rxjs/Observable";

@Injectable()
export class DashboardGuardService implements CanActivate {


  constructor(private router: Router,
              private cookieService: CookieService) {

  }

  private isAuthenticated() {

    const status: boolean = this.cookieService.check("auth");

    if (!status) {
      console.log("Not allowed to dashboard without login");
      this.router.navigate(["login"]);
    } else {
      console.log("Auth exists");
      return true
    }
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean | Observable<boolean> | Promise<boolean> {

    return this.isAuthenticated();
  }


}
