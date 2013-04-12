from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.utils import timezone
from django.core import serializers
from letter.models import Recommendation
import os

def recLetter(request):
    recs=Recommendation.objects.filter(type='rec')
    return render(request, 'recLetter.html',{'letters': recs})    

def conLetter(request):
    cons=Recommendation.objects.filter(type='con')
    return render(request, 'conLetter.html',{'letters': cons})    

def home(request):
    return render(request, 'home.html')

def recondemnation(request):
    return render(request, 'recondemnation.html')

def submit(request):
    _type=""
    if request.method == 'POST':
        _name=request.POST.get('name', 0)
        _rec=request.POST.get('rec',0)
        _type=request.POST.get('type',0)    
        rec=Recommendation(name=_name,rec=_rec,type=_type)
        rec.save()
    if _type=="con":
        cons=Recommendation.objects.filter(type='con')
        return render(request, 'recSubmit.html',{'letters': cons})    
    else:
        recs=Recommendation.objects.filter(type='rec')
        return render(request, 'recSubmit.html',{'letters': recs})    

