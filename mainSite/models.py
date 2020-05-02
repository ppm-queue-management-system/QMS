from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class BookTicketModel(models.Model):
    post = models.CharField(max_length=10)

class AdjustTicketModel(models.Model):
    post = models.CharField(max_length=10)
    
class CancelTicketModel(models.Model):
    post = models.CharField(max_length=10)
