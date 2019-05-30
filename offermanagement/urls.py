"""offermanagement URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from community.views import *
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('write/', write, name="write"),
    path('list/', list, name="list"),
    path('view/<num>/', view),
    url(r'^view/(?P<num>[0-9]+)/$', view), # in case of using regular expression
]
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from bookmark.bmviews import bmdetail, bmhome, omtest
from community.views import list, view, write

urlpatterns = [
    # start page(http://localhost)
    # path('', views.home),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^write/', write, name='write'),
    path('admin/', admin.site.urls),
    path('write/', write, name="write"),
    path('list/', list, name="list"),
    path('view/<num>/', view, name="view"),
    path('bmhome/', bmhome),
    path('bmdetail/', bmdetail),
    path('omtest/', omtest),
]
