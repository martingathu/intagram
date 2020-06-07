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
    like = models.IntegerField(default=0)

    @classmethod
    def get_posts(cls):
        posts = cls.objects.all()
        return posts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    class Meta:
        ordering = ['pub_date']
    
    @classmethod
    def update_post(self, update):
        self.post = update
        self.save

    @classmethod
    def display_user_post(cls):
        post = cls.objects.filter()
        return post
class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return '{} follows {}'.format(self.following,self.follower)

User.add_to_class('followings',models.ManyToManyField('self',through=Follow,related_name='followers',symmetrical=False))
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_photo = models.ImageField(upload_to = 'posts/')
    bio = models.TextField(max_length=255)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def updateProfile(self, update):
       self.bio = update
       self.save

    @classmethod
    def search_profile(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user 

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(id=id)
        return profile