from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=155,primary_key=True)
    def __str__(self):
        return self.topic_name
    
class WebPage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=140)
    url=models.URLField()
    email=models.EmailField(default='charanbkumar143@gmail.com')

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name=models.ForeignKey(WebPage,on_delete=models.CASCADE)
    author=models.CharField(max_length=150)
    date=models.DateField()

    def __str__(self):
        return self.author
