from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from post.models import Post


# uploading user files to a specific directory
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="profile_pciture", null=True, default="default.jpg")
    favourite = models.ManyToManyField(Post, blank=True)
    
    
    # def __str__(self):
    #     return User.username