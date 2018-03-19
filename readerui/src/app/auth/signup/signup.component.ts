import {Component, OnInit} from "@angular/core";
import {EmailValidator, FormBuilder, FormGroup, Validators} from "@angular/forms";
import {Router} from "@angular/router";
import {AlertService} from "../../alert/alert.service";
import {AuthService} from "../auth.service";

@Component({
  selector: 'signup',
  templateUrl: 'signup.component.html'
})

export class SignupComponent implements OnInit {

  public signupForm: FormGroup;

  constructor(private formbuilder: FormBuilder,
              private router: Router,
              private alertService: AlertService,
              private authService: AuthService) {

  }


  ngOnInit() {
    console.log("Signup init started");

    this.createForm();
  }

  private createForm() {

    this.signupForm = this.formbuilder.group({
      'username': ['', [Validators.required, Validators.minLength(8), Validators.maxLength(30)]],
      'first_name': ['', [Validators.required, Validators.minLength(5), Validators.maxLength(60)]],
      'last_name': ['', [Validators.required, Validators.minLength(5), Validators.maxLength(60)]],
      'email': ['', [EmailValidator,]],
      'phone_number': ['']
    })
  }


  public submit(data: any) {
    this.alertService.reset();
    console.log("Signup data", data);


    this.authService.signup(data).then(response => {
      console.log(response);
      this.alertService.success("Successfully Registered. Please wait for admin to activate");
      this.signupForm.reset();

    }).catch(error => {
      console.log(error);
      this.alertService.error(error.error.message)
    });
  }


  public redirectToLogin() {
    this.router.navigate(['login'])
  }
}
