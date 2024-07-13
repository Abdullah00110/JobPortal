from django.db.models.signals import post_save
from django.contrib.auth.models import User
from accounts.models import Education
from django.dispatch import receiver
from accounts.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) :
    if created :
        print("SIGNAL IS WORKING FINE --->", "IN IF BLOCK")
        Profile.objects.create(user=instance)
    else :
        print("SIGNAL IS WORKING FINE --->", "IN ELSE BLOCK")
        instance.profile.save()