from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.fake_login, name='fake_login'),
    path('vulnerable/', views.fake_vulnerable_endpoint, name='fake_vulnerable_endpoint'),
]
