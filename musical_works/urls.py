"""musical_works URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from musical_works.works.models import Work
from musical_works.works.views import (
    ContributorViewSet,
    WorkViewSet,
)

router = routers.DefaultRouter()
router.register("works", WorkViewSet, base_name=Work)
router.register("contributors", ContributorViewSet)

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"", include(router.urls))]
