from django.db import models

# Create your models here.
class SigninModel(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=50)

class BookTicketModel(models.Model):
    post = models.CharField(max_length=10)

class AdjustTicketModel(models.Model):
    post = models.CharField(max_length=10)
    
class CancelTicketModel(models.Model):
    post = models.CharField(max_length=10)
    
