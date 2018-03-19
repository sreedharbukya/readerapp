import {Component, OnInit} from "@angular/core";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {AuthService} from "../auth.service";
import {AlertService} from "../../alert/alert.service";
import {CookieService} from "ngx-cookie-service";

@Component({
  selector: 'login',
  templateUrl: 'login.component.html'
})

export class LoginComponent implements OnInit {

  public loginForm: FormGroup;

  constructor(private formBuilder: FormBuilder,
              private router: Router,
              private authService: AuthService,
              private alertService: AlertService,
              private cookieService: CookieService) {

  }


  ngOnInit() {
    console.log("Successfully login page started");
    this.cookieService.deleteAll();
    this.buildLoginForm();
  }


  private buildLoginForm() {
    this.loginForm = this.formBuilder.group({
      username: ['', [Validators.required]],
    })
  }

  public submit(data: any) {
    this.alertService.reset();
    console.log("Data submitted", data);
    this.authService.login(data).then(response => {
      console.log(response);
      this.alertService.success("Successfully logged in.");

      this.router.navigate(['dashboard']);

    }).catch(error => {
      console.log(error);
      this.alertService.error("Invalid Credentials")
    });
  }

  public redirectToSingup() {
    this.router.navigate(['signup'])
  }

}
