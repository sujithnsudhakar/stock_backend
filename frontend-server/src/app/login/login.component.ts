import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../service/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  public loginForm !: FormGroup;

  userData !: any;

  errorMessage !: any;

  constructor(private formBuilder : FormBuilder, 
    private api: ApiService,
    private router:Router) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      userName:[''],
      userPassword:['']
    })
  }

  login(){
    this.router.navigate(['dashboard'])
    }
}