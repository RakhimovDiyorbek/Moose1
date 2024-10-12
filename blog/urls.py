from django.urls import path
from .views import index, article, about, contact, detail, home

urlpatterns = [
    path('', index, name='index'),
    path('article/', article, name='article'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('article/<int:pk>/', detail, name='detail'),
    path('home/', home, name='home')
]
