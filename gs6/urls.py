"""
URL configuration for gs5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from api import views
from api.views import (
    ItemCreateView, ItemRetrieveView, ItemUpdateView, ItemDeleteView,
    CustomTokenObtainPairView,
)
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('admin/', admin.site.urls),
    path('items/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/', ItemRetrieveView.as_view(), name='item-detail'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
