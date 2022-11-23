
from django.urls import path
from core import views
from user import views


app_name = "user"

urlpatterns = [
    path("signup/", views.UserCreateView.as_view(), name = "user_signup"),
    path("login/", views.UserLoginView.as_view(), name = "user_login"),
    path("logout/", views.UserLogoutView.as_view(), name = "user_logout"),

    # PROFILE 
    path("profile/create", views.ProfileCreateView.as_view(), name="profile_create"),
    path("profile/detail", views.ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/",views.ProfileUpdateView.as_view(),name="profile_update"), 
    


    #freelancer registration 
    path("freelancerregistartion/",views.freelancerregistartion.as_view(), name="freelancerregistartion"),
    path("freelancersignup/",views.FreelancerCreateView.as_view(), name="freelancersignup"),
    path("freelancerproinfo/",views.FreelancerProView.as_view(), name="freelancerproinfo"),
    path("freelancerlinkacc/",views.FreelancerlinkaccView.as_view(), name="freelancerlinkacc"),
    #path("freelancerportfolio/",views.FreelancerportfolioView.as_view(), name="freelancerportfolio"),
    path("FreelancerCreate/",views.FreelancerCreateView.as_view(), name="becomeafreelancer"),
    path("freelancer/<int:pk>/update/",views.FreelancerUpdateView.as_view(), name="Freelancerupdate"),
]   


