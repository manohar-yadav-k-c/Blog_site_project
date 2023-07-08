from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_model(models.Model):
    models.OneToOneField(User,on_delete=models.CASCADE)
       
class post_model(models.Model):
    description=models.CharField(max_length=1000,blank=True)
    image=models.FileField(upload_to='images/',blank=True)
    date=models.DateTimeField(blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.user.username