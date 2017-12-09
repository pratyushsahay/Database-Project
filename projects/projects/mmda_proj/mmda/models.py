from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


#class Choice(models.Model):
#    def __str__(self):
#        return self.choice_text


class File(models.Model):
    filename = models.CharField(max_length=200)
    annotated_name = models.CharField(max_length=200)
    storage_path = models.CharField(max_length=200)
    GUID = models.IntegerField(default=0)
    filetype = models.CharField(max_length=200)
    def __str__(self):
        return self.filename

class Creation_Metadata(models.Model):
    creator_name = models.CharField(max_length=200)
    creation_time = models.DateTimeField('Creation time')
    last_modified = models.DateTimeField('Last modified')
    def __str__(self):
        return self.choice_text

class Document(models.Model):
    file_size = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)

class Image(models.Model):
    resolution = models.CharField(max_length=200)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)

class Webpage(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.title



