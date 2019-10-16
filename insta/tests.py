from django.test import TestCase
from .models import Image
# # Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.image=Image(name='index',)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        category = Image.objects.all()
        self.assertTrue(len(image) == 0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='profile',)
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)