from django.test import TestCase
from .models import Post,Profile,Comment
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    a class to test the profile instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='martin')
        self.profile= Profile(profile_photo='/static/images/log.png',bio='dev',user=self.user)
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))
        
    #Testing the save method
    '''
    function to check the save method of profile
    '''
    
    def test_save_method(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>=1)
        
    #Testing the delete method
    def test_delete_method(self):
        '''
        function to check the delete method of profile
        '''
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_photo='/static/images/log.png').first()
        delete= Profile.objects.filter(profile_photo=profil.profile_photo).delete()
        profile=Profile.objects.all()
        self.assertFalse(len(profile)==1)

    #Testing the update method
    def test_update_profile(self):
        '''
        a method that helps to update the profile
        
        ''' 
        self.profile.save_profile()
        profil= Profile.objects.filter(profile_photo='/static/images/log.png').first()
        update = Profile.objects.filter(profile_photo=profil.profile_photo).update(profile_photo='pic')
        updated = Profile.objects.filter(profile_photo='pic').first()
        self.assertNotEqual(profil.profile_photo,updated.profile_photo)
        
        
class PostTestClass(TestCase):
    '''
    a class to test the image instances and its methods
    '''

    # Set up method
    def setUp(self):
        self.user = User.objects.create(id=1,username='martin')
        self.post_image= Post(post_image='/static/images/log.png',caption='lovely',pub_date='2pm',like='1',user=self.user)
    
 
    

        
 
   
            
            
