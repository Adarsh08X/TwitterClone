from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = models.ImageField(upload_to='uploads/', default='uploads/default.png')
    bio = models.TextField(blank=True, null=True)

User.twitterprofile = property(lambda u:Profile.objects.get_or_create(user=u)[0])
