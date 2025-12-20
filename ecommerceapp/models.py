from django.db import models
from .validators import validate_image_size

# Create your models here.
class uuser(models.Model):
    title = models.CharField(max_length=100,null='True')
    date = models.CharField(max_length=100,null='True')
    description = models.CharField(max_length=500,null='True')
    img = models.ImageField(upload_to='images/', validators=[validate_image_size],null = 'True')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    message = models.CharField(max_length=500)


