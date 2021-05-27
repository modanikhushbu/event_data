from django.db import models

# Create your models here.

class Unintresting_url(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url

class Interesting_url(models.Model):
    url = models.URLField(primary_key= True)
    title = models.CharField(max_length=100)
    date_and_time = models.CharField(max_length=100)
    interested_group = models.CharField(max_length=50)

    def __str__(self):
        return self.title



    