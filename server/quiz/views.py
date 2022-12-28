from django.shortcuts import render
from rest_framework import viewsets, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response

from quiz.models.questions import Question
from quiz.serializers import QuestionSerilizer

# Create your views here.
class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerilizer
    
class ResultsView(viewsets.GenericViewSet):
    @action(detail=False, methods=["post"])
    def result(self, request):
        answers = request.data
        if not isinstance(answers, list) or any(not isinstance(i,int) for i in answers): 
            raise exceptions.APIException("please submit an array of integars", 400)
        number_of_questions = len(answers)
        max_points = number_of_questions * 100
        points = 0
        for answer in answers:
            points += answer * 25
        if points <= max_points / 2:
            return Response({ "result": "Introvert" })
        return Response({ "result": "Extrovert" })
