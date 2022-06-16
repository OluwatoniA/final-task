"""kodecamp7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from HMS import views

urlpatterns = [
    path('', views.home, name='home'),
    path('occupant_data/', views.occupant_data, name='occupant_data'),
    path('add_occupants/', views.add_occupants, name='add_occupants'),
    path('update_data/<str:pk>/', views.update_data, name="update_data"),
    path('delete_data/<str:pk>/', views.delete_data, name="delete_data"),
    path('admin/', admin.site.urls)
]