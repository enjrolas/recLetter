from django.db import models

class Recommendation(models.Model):
    name=models.TextField()
    rec=models.TextField()
    type=models.TextField()
    date=models.DateField(auto_now=True)
    
