"""xml_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from xml_data import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.get_list_of_titles, name="list_of_titles"),
    path('title/<str:title_number>', views.read_single_title, name="read_single_title"),
    path('title/<str:title_number>/<str:section_number>', views.section_details, name="section_details"),
    path('title/search-title', views.search_title, name="search_title"),
]
