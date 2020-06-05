from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Profile, Post, Comment
from django.contrib.auth.models import User


class PostTestClass(TestCase):
    def setUp(self):
        self.post = Post(caption = 'mynewshoe',)

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.asserTrue(len(post)>0)

    def test_delete_images(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.asserTrue(len(post) == 0)