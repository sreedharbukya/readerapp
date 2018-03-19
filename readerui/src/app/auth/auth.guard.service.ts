import {Injectable} from "@angular/core";
import {CanActivate, Router} from "@angular/router";
import {Observable} from "rxjs/Observable";
import {AuthService} from "./auth.service";

@Injectable()
export class AuthGuardService implements CanActivate {


  constructor(private router: Router,
              private authService: AuthService) {
  }

  canActivate(): Observable<boolean> | Promise<boolean> | boolean {

    const status: boolean = this.authService.isAuthenticated();

    if (!status) {
      this.router.navigate(['login']);
    }
    return status
  }
}
