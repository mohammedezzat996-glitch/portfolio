from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects_gallery, name='gallery'),
    path('projects/<int:pk>/', views.project_detail, name='detail'),
    path('message/delete/<int:pk>/', views.delete_message, name='delete_message'),
]