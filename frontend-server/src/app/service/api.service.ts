import { Injectable } from '@angular/core';
import {HttpClient, HttpClientModule} from '@angular/common/http'
import {map} from 'rxjs/operators'

@Injectable({
  providedIn: 'root'
})

export class ApiService {

  constructor(private http: HttpClient) { }

  get(){
    return this.http.get<any>("http://localhost:8080/role")
    .pipe(map((res:any)=>{
      return res;
    }))
  }

  post(data : any){
    return this.http.post<any>("http://localhost:8080/news", data)
    .pipe(map((res:any)=>{
      return res;
    }))
  }

  delete(id : number){
    return this.http.delete<any>("http://localhost:8080/news/"+id)
    .pipe(map((res:any)=>{
      return res;
    }))
  }

  update(data : any, id:number){
    return this.http.put<any>("http://localhost:8080/news/"+id, data)
    .pipe(map((res:any)=>{
      return res;
    }))
  }
}