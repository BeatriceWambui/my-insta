from django.test import TestCase
from .models import Image
# # Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        self.image=Image(name='index',)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_category(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image.delete_image()
        category = Image.objects.all()
        self.assertTrue(len(image) == 0)
