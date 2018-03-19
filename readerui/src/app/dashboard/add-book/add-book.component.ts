import {Component, OnInit} from "@angular/core";
import {FormBuilder, FormGroup, Validators} from "@angular/forms";
import {DashboardService} from "../dashboard.service";
import {AlertService} from "../../alert/alert.service";

@Component({
  selector: 'add-book',
  templateUrl: 'add-book.component.html'
})
export class AddBookComponent implements OnInit {
  public bookForm: FormGroup;


  constructor(private formBuilder: FormBuilder,
              private dashboardService: DashboardService,
              private alertService: AlertService) {

  }

  ngOnInit() {

    this.createForm();

  }


  private createForm() {

    this.bookForm = this.formBuilder.group({
      'title': ['', [Validators.required, Validators.minLength(5), Validators.maxLength(60)]],
      'isbn_number': ['', [Validators.required, Validators.minLength(13), Validators.maxLength(13)]]
    })

  }

  public submit(data: any) {
    this.alertService.reset();
    console.log("Data Submitted", data);


    this.dashboardService.create_book(data).then(response => {
      console.log(response);

      this.bookForm.reset();
      this.alertService.success("Successfully added book with ISBN" + response.isbn_number);


    }).catch(error => {

      console.log("Error ", error);
      this.alertService.error("Failed to create Book");

    })


  }


}
