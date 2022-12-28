import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { lastValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GetQuestionsService {

  constructor(
    private http: HttpClient
  ) { }

  async getQuestions(){
    return await lastValueFrom(this.http.get('http://localhost:8000/api/question'))
  }
}
