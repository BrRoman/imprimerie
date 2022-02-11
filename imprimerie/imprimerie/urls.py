""" imprimerie/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('imprimerie/', include('apps.main.urls')),
    path('imprimerie/jobs/', include('apps.jobs.urls')),
    path('imprimerie/elements/', include('apps.elements.urls')),
    path('imprimerie/clients/', include('apps.clients.urls')),
    path('imprimerie/papers/', include('apps.papers.urls')),
    path('imprimerie/accounts/', include('apps.accounts.urls')),
    path('imprimerie/admin/', admin.site.urls),
]
