import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { GetQuestionsService } from 'src/services/get-questions.service';
import { GetResultService } from 'src/services/get-result.service';

@Component({
  selector: 'app-quiz-page',
  templateUrl: './quiz-page.component.html',
  styleUrls: ['./quiz-page.component.css']
})
export class QuizPageComponent implements OnInit {
  result: any
  constructor(
    private getQuestionService: GetQuestionsService,
    private getResultService: GetResultService,
    private router: Router
  ) { }

  async ngOnInit(): Promise<void> {
    this.result = await this.getQuestionService.getQuestions()
    // this.quizForm.valueChanges?.subscribe(event => console.log(this.quizForm))
    console.log(this.result);
  }

  async onSubmit(form: NgForm){
    let response = await this.getResultService.getResult(Object.values(form.value))
    console.log(response);
    
    this.router.navigate(['/result'], {state: {result: response.result}})
  }


}
