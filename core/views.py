from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from core import models as core_models
from core.forms import FeedbackForm
from django.views import generic as views
from user import models as user_models


# Create your views here.
class HomeView(views.TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        freelancers = user_models.FreelancerModel.objects.filter()
        context["freelancers"] = freelancers
        return context


class AboutView(views.TemplateView):
    template_name = "core/about_us.html"
    extra_content = {}


# feedbackview
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    model = core_models.FeedbackModel
    form_class = FeedbackForm
    success_url = reverse_lazy("core:home")


class FeedbackListView(views.TemplateView):
    template_name = "core/feedback/feedback_list.html"
    model = core_models.FeedbackModel


# freelancerview


class freelancerregistartion(views.TemplateView):
    template_name = "core/freelancer/freelancerregistartion.html"
    extra_content = {}


# class FreelancerCreateView(views.TemplateView):
#     template_name="core/freelancer/freelancersignup.html"
#     extra_content={

# }
# class FreelancerProView(views.TemplateView):
#     template_name="core/freelancer/freelancerproinfo.html"
#     extra_content={

# }
# class FreelancerlinkaccView(views.TemplateView):
#     template_name="core/freelancer/freelancerlinkacc.html"
#     extra_content={
#         }
class FreelancerportfolioView(views.TemplateView):
    template_name = "core/freelancer/freelancerportfolio.html"
    extra_content = {}


class FreelancerPayment(views.TemplateView):
    template_name = "core/payment/payment.html"
    extra_content = {}


# class FreelancerPricing(views.TemplateView):
#     template_name="core/freelancer/freelancerpricing.html"
#     extra_content={
#         }


class BuyerRequirements(views.TemplateView):
    template_name = "core/payment/requirements.html"
    extra_content = {}
