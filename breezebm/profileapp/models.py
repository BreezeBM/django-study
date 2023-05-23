from django.contrib.auth.models import User
from django.db import models


# request.user.profile로 바로 접근할 수 있도록 related_name 설정
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="profile/", null=True)
    nickname = models.CharField(max_length=255, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)
