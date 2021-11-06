""" apps/main/urls.py """

from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/update/', views.update, name='update'),
]
