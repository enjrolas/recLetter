from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from recommendation.models import Recommendation
import os

def recLetter(request):
    recs=Recommendation.objects.filter(type='recs')
    cons=Recommendation.objects.filter(type='cons')
    return render(request, 'conLetter.html',{recs: recs, cons: cons})    


def conLetter(request):
    recs=Recommendation.objects.filter(type='recs')
    cons=Recommendation.objects.filter(type='cons')
    return render(request, 'conLetter.html',{recs: recs, cons: cons})    

def home(request):
    return render(request, 'home.html')
