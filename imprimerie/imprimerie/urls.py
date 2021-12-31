""" imprimerie/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('imprimerie/', include('apps.main.urls')),
    path('imprimerie/tasks/', include('apps.tasks.urls')),
    path('imprimerie/clients/', include('apps.clients.urls')),
    path('imprimerie/papers/', include('apps.papers.urls')),
    path('imprimerie/accounts/', include('apps.accounts.urls')),
    path('imprimerie/admin/', admin.site.urls),
]
