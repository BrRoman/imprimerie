""" apps/papers/admin.py """

from django.contrib import admin
from .models import Paper

admin.site.register(Paper)
