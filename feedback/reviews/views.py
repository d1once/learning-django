from reviews.models import Review
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(ListView):
    template_name = "reviews/thank_you.html"
    model = Review

    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=4)
    #     return data


class ReviewsListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        contex["reviews"] = reviews
        return contex


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
