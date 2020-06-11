from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home')
]
