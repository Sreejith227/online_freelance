from django import forms
from user import models as user_models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


USER = get_user_model()

# User Registration Form
class UserRegisterform(UserCreationForm):
    class Meta:
        model = USER
        fields = ["email", "username"]


# Profile Form

class ProfileForm(forms.ModelForm):
    class Meta:
        model = user_models.ProfileModel
        exclude = (
            "status",
            "created_on",
            "updated_on",
        )

class AddressForm(forms.ModelForm):
    class Meta:
        model = user_models.AddressModel
        exclude = ("status",)
          

        #  FREELANCER FORM  
class FreelancerForm(forms.ModelForm):
    class Meta:
        model= user_models.FreelancerModel
        exclude = (
           
        )
