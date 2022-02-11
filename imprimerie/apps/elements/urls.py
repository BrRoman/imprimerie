""" apps/elements/urls.py """

from django.urls import path

from . import views

app_name = 'elements'
urlpatterns = [
    path('create/job=<int:job>/', views.create, name='create'),
    path('<int:pk>/', views.details, name='details'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
