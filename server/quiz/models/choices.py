from django.db import models

from quiz.models.questions import Question

class Choice(models.Model):
    value = models.IntegerField()
    text = models.TextField()
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        blank=False,
        related_name='choices',
        null=False
    )