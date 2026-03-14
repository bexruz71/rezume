from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand,Portfolio,Discount,Resume,Awards,About,Comment,Service,Blog,Contact
from .forms import ContactForm


def home_page(request):
    brands = Brand.objects.all()
    portfolio = Portfolio.objects.all()
    discount = Discount.objects.all()
    resume = Resume.objects.all()
    awards = Awards.objects.all()
    about = About.objects.all()
    comment = Comment.objects.all().order_by('-created_date')


