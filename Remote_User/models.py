from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class sentiment_prediction(models.Model):

    tweetURL= models.CharField(max_length=3000)
    tweetID= models.CharField(max_length=3000)
    tdate= models.CharField(max_length=3000)
    tweetContent= models.CharField(max_length=30000)
    userLocation= models.CharField(max_length=3000)
    retweetCount= models.CharField(max_length=3000)
    likeCount= models.CharField(max_length=3000)
    tweetLanguage= models.CharField(max_length=3000)
    sourceLabel= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



