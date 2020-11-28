from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_superuser',views.create_superuser),
    path('create_adminuser',views.create_adminuser),
    path('create_normaluser',views.create_normaluser),
]