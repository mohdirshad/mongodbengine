from django.db import models
from djangotoolbox.fields import ListField
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=400 ,)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now_add=True)
    tags = ListField()
    comments = ListField()


    def __unicode__(self):
    	return self.title






