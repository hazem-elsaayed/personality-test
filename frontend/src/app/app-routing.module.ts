import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { QuizPageComponent } from './quiz-page/quiz-page.component';
import { ResultPageComponent } from './result-page/result-page.component';

const routes: Routes = [
  { path: '', component: LandingPageComponent },
  { path: 'quiz', component: QuizPageComponent },
  { path: 'result', component: ResultPageComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
