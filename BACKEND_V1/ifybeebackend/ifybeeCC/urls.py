from django.urls import path
from . import views

app_name = 'ifybeeCC'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('academy/', views.academy_view, name='academy'),
    path('about/', views.about_view, name='about'),
]

