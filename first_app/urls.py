from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-view/', views.ObjectCreate.as_view(), name='create-view')
]