from rest_framework import serializers

from quiz.models.choices import Choice
from quiz.models.questions import Question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice 
        fields = ['value', 'text']


class QuestionSerilizer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ['text', 'choices']
    
    def create(self, validated_data):
        choices_data = validated_data.pop('choices')
        question = Question.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(question=question, **choice_data)
        return question
        