from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'commentaire'

urlpatterns = [
    path('', views.CommentListView.as_view(), name='list'),
    path('<int:pk>/', views.CommentDetailView.as_view(), name='detail'),
]