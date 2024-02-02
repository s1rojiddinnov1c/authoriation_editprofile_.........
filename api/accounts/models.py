from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta
import datetime




class User(AbstractUser):
    email = models.EmailField(null= True, blank=True)
    photo =  models.ImageField( upload_to="user_photo/",
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "svg", "heic", "heif", "webp"]
            )
        ],
    )
    



    @property
    def full_name(self):
        return f"{self.username}"
    
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {"access": str(refresh.access_token),"refresh": str(refresh)}


class UserConfirmation(User):
    CODE_LIFETIME = 3 #code lifetime in minutes
    code = models.CharField(max_length = 10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'verify_code')
    code_lifetime = models.DateTimeField(null=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username} -> {self.code}"
    
    def save(self, *args, **kwargs):
        self.code_lifetime = datetime.now() + timedelta(minutes=self.CODE_LIFETIME)
        super(UserConfirmation, self).save(*args, **kwargs)