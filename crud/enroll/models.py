from django.db import models

# Create your models here.
class userProfile(models.Model):

    name= models.CharField(max_length=20)
    email= models.EmailField()
    password= models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'
