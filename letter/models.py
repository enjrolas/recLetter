from django.db import models
from datetime import datetime

class Recommendation(models.Model):
    name=models.TextField()
    rec=models.TextField()
    type=models.TextField()
    dateAdded=models.DateTimeField(auto_now=True)
