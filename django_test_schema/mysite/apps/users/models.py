from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model,
    TextChoices,
    OneToOneField,
    CharField,
    DateField,
    CASCADE,
)

class User(AbstractUser):
    class Meta:
        db_table = 'users'
        managed = True

class UserProfile(Model):
    class Gender(TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        __empty__ = "(Unknown)"

    user = OneToOneField(User, on_delete=CASCADE)
    gender = CharField(
        max_length=1, choices=Gender.choices, default=Gender.__empty__
    )
    date_of_birth = DateField(blank=True, null=True, default=None)

    class Meta:
        db_table = 'user_profiles'
        managed = True