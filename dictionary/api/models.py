# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class dictionary(models.Model):
    word=models.CharField(max_length=200)
    meaning=models.CharField(max_length=200)

    def __str__(self):
       return self.word
