from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=264)
    link = models.URLField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta():
        ordering = ['-pk']
