# Create your views here.
from email import message
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import forms as auth_forms

from user.forms import UserRegisterform, ProfileForm
from user import models as user_models


USER = get_user_model()

# UserCreateView
class UserCreateView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = UserRegisterform
    success_url = reverse_lazy("user:user_login")


   

class UserLoginView(views.View):
    form_class = auth_forms.AuthenticationForm
    success_url = reverse_lazy("core:home")
    template_name = "registration/login.html"

    def get(self, request):
        context = {
            "form": self.form_class(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request=request)
        # if form.is_valid():
        form.is_valid()
        username = request.POST.get("username")
        password = request.POST.get("password")
        # to check whether the given username and password are exists or not
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # to login user
            login(request, user)
            print("USER is valid.............LOGGED IN")
            return redirect(self.success_url)
        print("USER is not valid.............")
        print("FORM is not valid.............")
    

        context = {"form": form}
        return render(request, self.template_name, context)

class UserLogoutView(views.View):
    template_name="registration/logout.html"
    def get(self,request):
        logout(request)
        return render(request,self.template_name)

# PROFILE CREATE UPDATE DELETE
class ProfileCreateView(views.CreateView):
    template_name = "core/profile/profile_create.html"
    model = user_models.ProfileModel
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile_detail")


class ProfileUpdateView(views.UpdateView):
    template_name = "core/profile/profile_update.html"
    model = user_models.ProfileModel
    form_class = ProfileForm
    success_url = reverse_lazy("user:profile_detail")

    

class ProfileDetailView(views.TemplateView):
    template_name = "core/profile/profile.html"
    model = user_models.ProfileModel
    context_object_name = "profile"

   # ------PROFILE VIEW -------#


  #------FREELANCER REGISTRATION ------#
class freelancerregistartion(views.TemplateView):
    template_name="core/freelancer/freelancerregistartion.html"  
    extra_content={} 
    
class FreelancerCreateView(views.TemplateView):
    template_name="core/freelancer/freelancersignup.html"  
    extra_content={

} 
   

class FreelancerProView(views.TemplateView):
    template_name="core/freelancer/freelancerproinfo.html"  
    extra_content={

    }  
    
class FreelancerlinkaccView(views.TemplateView):
    template_name="core/freelancer/freelancerlinkacc.html"  
    extra_content={

    }
    

class FreelancerPricing(views.TemplateView):
    template_name="core/freelancer/freelancerpricing.html"  
    extra_content={
        }
