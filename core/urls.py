from django.urls import path
from core import views
app_name="core"

urlpatterns=[
    path("",views.HomeView.as_view(),name="home"),
    
    path("about_us/",views.AboutView.as_view(), name="about_us"),
    path("feedback/create/", views.FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedback_list/",views.FeedbackListView.as_view(), name="feedback_list"),
    path("freelancerregistartion/",views.freelancerregistartion.as_view(), name="freelancerregistartion"),
    # path("freelancersignup/",views.FreelancerCreateView.as_view(), name="freelancersignup"),
    # path("freelancerproinfo/",views.FreelancerProView.as_view(), name="freelancerproinfo"),
    # path("freelancerlinkacc/",views.FreelancerlinkaccView.as_view(), name="freelancerlinkacc"),
    path("freelancerportfolio/",views.FreelancerportfolioView.as_view(), name="freelancerportfolio"),
    path("payment/",views.FreelancerPayment.as_view(), name="payment"),
    path("requirements/",views.BuyerRequirements.as_view(), name="requirements"),
    # path("freelancerpricing/",views.FreelancerPricing.as_view(), name="freelancerpricing"),
   
    
]   