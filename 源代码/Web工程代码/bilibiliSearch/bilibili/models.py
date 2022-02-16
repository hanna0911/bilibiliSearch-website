from django.db import models


# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    moviename = models.CharField(max_length=256)
    movielink = models.CharField(max_length=128)
    moviedescription = models.CharField(max_length=1024)
    moviepicture = models.CharField(max_length=256)
    movieview = models.CharField(max_length=64)
    moviepop = models.CharField(max_length=64)
    moviedate = models.CharField(max_length=64)
    movielike = models.CharField(max_length=64)
    moviecoin = models.CharField(max_length=64)
    moviecollect = models.CharField(max_length=64)
    shareInfo = models.CharField(max_length=64)
    moviecomment1 = models.CharField(max_length=1024)
    moviecomment2 = models.CharField(max_length=1024)
    moviecomment3 = models.CharField(max_length=1024)
    moviecomment4 = models.CharField(max_length=1024)
    moviecomment5 = models.CharField(max_length=1024)
    username = models.CharField(max_length=64)
    userlink = models.CharField(max_length=128)
    userdescription = models.CharField(max_length=256)
    userfan = models.CharField(max_length=64)
    userpicture = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Movies from bilibili'

    def __str__(self):
        return self.moviename


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    userlink = models.CharField(max_length=128)
    userdescription = models.CharField(max_length=256)
    userfan = models.CharField(max_length=64)
    userpicture = models.CharField(max_length=256)
    movies = models.ManyToManyField(to='Movie')

    class Meta:
        verbose_name_plural = 'Users from bilibili'

    def __str__(self):
        return self.username
