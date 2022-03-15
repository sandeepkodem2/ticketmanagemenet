from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
STATUS_CHOICES=(
    
    ('CLOSED','closed'),
    ('IN_PROGRESS','in progress')
)

class Ticket(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title=models.CharField(max_length=126)
    description=models.TextField()
    status=models.CharField(choices=STATUS_CHOICES,max_length=100,default=STATUS_CHOICES[1][0])


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('apolloapp:detail',kwargs={'pk':self.pk})


    
