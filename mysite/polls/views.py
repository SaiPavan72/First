from django.shortcuts import render

from django.http import HttpResponse
from polls.models import  Question


def index(request):
    q = Question.objects.order_by('-pub_date')[0:5]
    return render(request,'polls/index.html',{'questions':q})
