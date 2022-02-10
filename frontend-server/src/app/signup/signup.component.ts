import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  public signupForm !: FormGroup;
  roleData !: any;

  userData !: any;

  constructor(private formBuilder : FormBuilder, 
    private router:Router) { }

  ngOnInit(): void {
    this.signupForm = this.formBuilder.group({
      userName:[''],
      userRole:[''],
      userPassword:['']
    })
  }


  signUp(){
      this.router.navigate(['login']);

  }

}