""" imprimerie/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('imprimerie/', include('apps.main.urls')),
    path('imprimerie/admin/', admin.site.urls),
]
