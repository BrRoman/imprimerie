""" apps/elements/admin.py """

from django.contrib import admin
from .models import Element

admin.site.register(Element)
