from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #indicate to the database that Question is a foriegn key and there is relation between choice and question
    
    choice_text = models.CharField(max_length=200)
    #This field is of type character field and its required prop is max_length
    
    votes = models.IntegerField(default=0)