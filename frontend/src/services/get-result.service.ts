import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { lastValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetResultService {

  constructor(
    private http: HttpClient
  ) { }

  async getResult(reqBody: object): Promise<any>{
    return await lastValueFrom(this.http.post("http://localhost:8000/api/result", reqBody))
  }
}
