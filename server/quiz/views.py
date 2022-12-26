from django.shortcuts import render
from rest_framework import viewsets

from quiz.models.questions import Question
from quiz.serializers import QuestionSerilizer

# Create your views here.
class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerilizer
