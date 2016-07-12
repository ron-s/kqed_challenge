"""food_trucks_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from rest_framework import routers
from food_trucks_app import views as food_trucks_app_views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'food_trucks_app_mobilefoodtrucks', food_trucks_app_views.MobileFoodTrucksViewSet) # name of the table

# Wire up our API using automatic URL routing.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', food_trucks_app_views.home_page),
    url(r'^food_trucks_app/', include(router.urls)), # name of the app
]

