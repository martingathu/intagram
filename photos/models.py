from django.db import models
import datetime as dt
from django.contrib.auth.models import User
import django.utils.timezone



# Create your models here.
class Post(models.Model):
    caption = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_image = models.ImageField(upload_to = 'posts/')

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE,)
#     profile_photo = models.ImageField(upload_to = 'posts/')
#     bio = models.TextField(max_length=255)

#     def save_profile(self):
#         self.save()

#     def delete_profile(self):
#         self.delete()

#     def updateProfile(sender, **kwargs):
#         if kwargs['created']:
#             profile = Profile.objects.created(user=kwargs['instance'])

#             post_save.connect(Profile, sender=User)