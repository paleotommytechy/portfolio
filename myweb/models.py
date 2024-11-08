from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    urls = models.URLField(max_length=200)

    def __str__(self):
        return self.title

class Testimonie(models.Model):
    author_name = models.CharField(max_length=40)
    author_position = models.CharField(max_length=20)
    comments = models.TextField()
    profile_img = models.ImageField(upload_to='images/author/')

    def __str__(self):
        return self.author_name
class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/myprofile')

    def __str__(self):
        return self.name