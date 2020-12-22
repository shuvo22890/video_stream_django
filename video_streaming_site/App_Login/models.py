from django.db import models
from django.contrib.auth.models import User
from App_Home.models import Video

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=264, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)

    def __str__(self):
        if self.full_name == '':
            return 'Anonymous'
        return self.full_name

class Review(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='review_video')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviewer')
    review = models.TextField(max_length=264)

    def __str__(self):
        return self.reviewer.full_name

    class Meta:
        ordering = ['-id']
