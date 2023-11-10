"""
URL configuration for sentrydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
import time


def trigger_error(request):
   try:
       division_by_zero = 1 / 0
   except:
       division_by_zero = "Hello World"

   return HttpResponse(division_by_zero)

def large_resource(request):
   time.sleep(4)
   return HttpResponse("Done!")

urlpatterns = [
   path('admin/', admin.site.urls),
   path('app/', include('names.urls')),
   path('sentry-debug/', trigger_error),
   path('large_resource/', large_resource),
]