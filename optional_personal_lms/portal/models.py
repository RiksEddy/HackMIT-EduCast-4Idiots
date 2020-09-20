from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Profile(models.Model):
    identity = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    department = models.CharField(max_length=50, null=False, blank=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        newuser=Profile()
        newuser.identity=instance

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Document(models.Model):
    title = models.CharField(max_length=30, blank=False)
    document = models.CharField(max_length=80,blank=False)
    message = models.TextField()
    uploaded_at = models.DateTimeField(default=datetime.now)
    # instructor = ....
    def __str__(self):
        return self.title



