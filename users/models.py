from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user         = models.OneToOneField(User, on_delete=models.CASCADE)
    bio          = models.TextField()
    first_name   = models.CharField(max_length=50, blank=True)
    last_name    = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user.username) + ' Profile'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)
        print('Profile Created')

post_save.connect(create_profile, sender = User)

def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()
        print('Profile Updated')

post_save.connect(create_profile, sender = User)
