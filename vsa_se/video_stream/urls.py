from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('video_display/<path:video_name>/', views.video_display, name='video_display'),
]