from django.conf.urls import include, url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^admin/', include(admin.site.urls)),
]
