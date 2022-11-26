from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from core import models as core_models




class CustomUser(AbstractUser):
    pass


USER = settings.AUTH_USER_MODEL


class LocationModel(core_models.TimeStamp, models.Model):
    lattitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.lattitude},{self.longitude}"


class AddressModel(core_models.TimeStamp, models.Model):

    building_name = models.CharField(max_length=64)
    place = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    district = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=24, default="India")
    postal_code = models.CharField(max_length=6)
    location = models.ForeignKey(
        LocationModel, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.building_name},{self.place}-{self.postal_code}"


class ProfileModel(core_models.TimeStamp, models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("T", "Transgender"),
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    dob = models.DateField()
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    image = models.ImageField(
        upload_to="user/profile/image/", default="default/user.png"
    )
    phone_number = models.CharField(max_length=15)
    email_id = models.CharField(max_length=150 , default="emailid")

    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".title()


class SkillModel(core_models.TimeStamp, models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class FreelancerFileModel(core_models.TimeStamp, models.Model):
    file = models.FileField(upload_to="user/freelancer/docs/", blank=True, null=True)

    def __str__(self):
        try:
            name = self.file.path
        except:
            name = "No File"
        return name


# -------------Freelancer registration-----------#
class FreelancerModel(core_models.TimeStamp, models.Model):
    class LanguageChoice(models.TextChoices):
        ENGLISH = "EN", "English"
        MALAYALAM = "ML", "Malayalam"

    cover_image = models.ImageField(
        upload_to="user/freelancer/cover_image/", default="default/user.png"
    )
    skills = models.ManyToManyField(SkillModel, blank=True)
    current_position = models.CharField(max_length=40)
    education = models.CharField(max_length=40)
    about_me = models.TextField(max_length=240)
    languages_known = models.CharField(
        max_length=20, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH
    )
    resume = models.FileField(
        upload_to="user/freelancer/resume/", blank=True, null=True
    )
    previous_projects = models.ManyToManyField(FreelancerFileModel, blank=True)
    facebook_id = models.CharField(max_length=100)
    twitter_id = models.CharField(max_length=100)
    google_id = models.CharField(max_length=100)
    instagram_id = models.CharField(max_length=100)
    maximum_delivery_time = models.FloatField(max_length=30 ,default = 1)
    price = models.FloatField(default=0.0)
    user = models.OneToOneField(USER, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} ({self.current_position})"
 
