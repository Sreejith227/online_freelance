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


# ========FREELANCER FORM==========
class FreelancerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        freelancer = getattr(self, "instance", None)
        # project_files = user_models.FreelancerFileModel.objects.filter(
        #     freelancermodel__in=[freelancer]
        # )
        project_files = getattr(freelancer, "previous_projects", None)
        if project_files:
            self.fields["previous_projects"] = forms.ModelMultipleChoiceField(
                queryset=project_files
            )

    class Meta:
        model = user_models.FreelancerModel
        exclude = ("user",)


# ======FREELANCER PROJECT FILE FORM=========
class FreelancerProjectFileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].label = "Add project files"

    class Meta:
        model = user_models.FreelancerFileModel
        fields = ["file"]
