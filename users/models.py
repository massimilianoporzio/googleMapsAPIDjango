from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# a One To One Profile to the User official model

class UserProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(verbose_name="Indirizzo", max_length=100, null= True, blank= True)
    town = models.CharField(verbose_name='Città/Paese',max_length=100, null=True,blank=True)
    county = models.CharField(verbose_name="Provincia", max_length=100,null=True,blank=True)
    post_cpde = models.CharField(verbose_name="CAP", max_length=100,null=True,blank=True)
    country = models.CharField(verbose_name="Stato",max_length=100, null=True, blank=True)
    longitude = models.CharField(verbose_name="Longitudine",max_length=50, null=True,blank=True)
    latitude = models.CharField(verbose_name="Latitudine", max_length=50, null=True, blank=True)

    captcha_score = models.FloatField(default=0.0)
    has_profile = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}'