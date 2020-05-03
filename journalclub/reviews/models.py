from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date Published')

    def __str__(self):
        return self.question_text


class Answers(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_test = models.CharField(max_length=1000)

    def __str__(self):
        return self.answer_test