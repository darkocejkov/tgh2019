"""insuredatasafe URL Configuration

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
"""
from django.contrib import admin
from django.urls import path

from pages import views

urlpatterns = [
    path('', views.index_view, name='index'),

    path('index/', views.index_view),
    path('elements/', views.elements_view),
    path('about/', views.about_view),

    path('index/elements', views.elements_view),
    path('index/about', views.about_view),
    path('index/index', views.index_view),

    path('about/elements', views.elements_view),
    path('about/index', views.index_view),
    path('about/about', views.about_view),

    path('elements/elements', views.elements_view),
    path('elements/index', views.index_view),
    path('elements/about', views.about_view),



    path('admin', admin.site.urls),
]
