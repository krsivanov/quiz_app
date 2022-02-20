from pyexpat import model
from statistics import mode
from django.db import models

from quizzes.models import Quiz

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=350)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)

    def get_answers(self):
      #  return self.answers.all()
      return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=350)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)# it can be done with related_name='answers')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}s"