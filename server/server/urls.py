from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from quiz import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(urls)),
]
