from django.urls import path
from . import views

urlpatterns = [
    path('home',views.blogList,name='home')
    # path('', views.home, name='home'),
    # path('about/', views.about, name='about'),
    # path('blog/', views.blog, name='blog'),
    # path('contact/', views.contact, name='contact'),
    # path('categories/', views.categories, name='categories'),
    # path('search/', views.search, name='search'),
    # path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    # path('social-media-links/', views.social_media_links, name='social_media_links'),
]