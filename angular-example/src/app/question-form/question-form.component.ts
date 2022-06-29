import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-question-form',
  templateUrl: './question-form.component.html',
  styleUrls: ['./question-form.component.css']
})
export class QuestionFormComponent implements OnInit {

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient
  ) { }

  ngOnInit(): void {
  }

  questionForm = this.formBuilder.group({
    questionType: 'single',
    text: '',
    correctAnswerOne: '',
    choiceOne: '',
    correctAnswerTwo: '',
    choiceTwo: '',
    correctAnswerThree: '',
    choiceThree: '',
    correctAnswerFour: '',
    choiceFour: '',
  });

  onSubmit(): void {
    const httpOptions = ({
        headers: new HttpHeaders({
            'Content-Type': 'application/json'
        })
    });

    this.http.post('/api/jsonadd',
        JSON.stringify(this.questionForm.value),
        httpOptions).subscribe();
  };

}
