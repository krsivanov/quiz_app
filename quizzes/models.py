from statistics import mode
from django.db import models
import random

# Create your models here.
# DIFF_CHOICES = (
#     ('Гражданско , Търговско, Административно право' , 'GTAp'),
#     ('Трудово и осигурително право', 'TOp'),
#     ('Данъчно право', 'Dp'),
#     ('Търговско и финансово управление на предприятието', 'TFup'),
#     ('Достъп до пазара', ''),
#     ('Технически стандарти и аспекти на дейността', 'TsAd'),
#     ('Безопасност на движението', 'BD'),
# )
DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)


class Quiz(models.Model):
    name = models.CharField(max_length=350)
    topic = models.CharField(max_length=350)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Duration in minutes")
    required_score = models.IntegerField(help_text="Score to pass in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.topic}'

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'