from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class myAPI(models.Model):
    owner = models.ForeignKey(User ,default = 1 , on_delete= models.CASCADE)
    apiurl = models.CharField(max_length=500, blank= False , null = False)
    post_data = models.TextField(max_length=10000 , blank = True , null = True)
    status = models.BooleanField(default = False)
    response_data = models.TextField(max_length=10000 , blank = True , null = True)
