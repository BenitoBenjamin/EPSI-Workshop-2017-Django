from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, primary_key=True)
    user_pref_1 = models.ForeignKey("Pref1")
    user_pref_2 = models.ForeignKey("Pref2")

class Pref1(models.Model):
    nom = model.CharField()

class Pref2(models.Model):
    nom = model.CharField()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()