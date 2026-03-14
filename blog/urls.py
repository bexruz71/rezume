from django.urls import path
from .views import home_page,contact_p

urlpatterns = [
    path('', home_page, name='home'),
    path('contact/', contact_p, name='contact'),
]
