from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Settings(models.Model):

    STATUS =(
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtp_server = models.CharField(blank=True, max_length=20)
    smtp_email = models.CharField(blank=True, max_length=20)
    smtp_password = models.CharField(blank=True, max_length=20)
    smtp_port = models.CharField(blank=True, max_length=20)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    about_us = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

