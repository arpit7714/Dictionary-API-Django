# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from api.models import dictionary
import json

# this method is used to manage the incoming word and meanging as they are dicectly get saved into the database
@csrf_exempt
def dictionary(request):
    if request.method=="POST":
       post=json.loads(request.body.decode("utf-8"))
       response_data={}
       if post.get("key") == "17147714":
          word1=post['word']
          meaning1=post['meaning']
          try:
             dictionary.objects.create(word=word1,meaning=meaning1)
             response_data['status']='success'
          except Exception as e:
                 response_data['status']=str(e)
    return HttpResponse(
          json.dumps(response_data),
          content_type = "application/json"
          )

#this method is used to get the meaning of the required word
@csrf_exempt
def getmeaning(request):
    response_data={}
    word1=request.GET.get('word')
    try:
       meaning1=dictionary.objects.get(word=word1)
       meaning=meaning1.meaning
       response_data['meaning']=meaning
    except Exception as e:
       response_data['meaning']="Not found in database"
    return HttpResponse(
           json.dumps(response_data),
           content_type="application/json"
    )
    
