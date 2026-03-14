from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand,Portfolio,Discount,Resume,Awards,About,Comment,Service,Blog,Contact
from .forms import ContactForm


def home_page(request):
    brand = Brand.objects.all()
    portfolio = Portfolio.objects.all()
    discount = Discount.objects.all()
    resume = Resume.objects.all()
    award = Awards.objects.all()
    about = About.objects.all()
    comment = Comment.objects.all().order_by('-created_date')
    service = Service.objects.all()
    blog = Blog.objects.all()
    contact = Contact.objects.all()
    context = {
        'brands': brand,
        'portfolios': portfolio,
        'discounts': discount,
        'resumes': resume,
        'awards': award,
        'abouts': about,
        'comments': comment,
        'services': service,
        'blogs': blog,
        'contacts': contact,
    }
    return render(request, 'index.html', context)


