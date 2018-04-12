from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

from searchdata import views

urlpatterns = [
    url(r'^$', views.api_root),
]