"""tech_test URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from user.views import *
from testing.views import *
from products.views import *
from sells.views import *
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Test Documentation",
        default_version='1.0.0',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger', schema_view.with_ui(
        'swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('api-auth', include('rest_framework.urls')),

    path('test/', TestListCreateView.as_view(), name='test'),
    path('test/<int:pk>', TestGetDeleteUpdateView.as_view(), name='test-detail'),

    path('product/', ProductListCreateView.as_view(), name='product'),
    path('product/<int:pk>', ProductGetDeleteUpdateView.as_view, name='product-detail'),

    path('sell-in-out/', SellInOutListCreateView.as_view(), name='sell-in-out'),
    path('sell-in-out/<int:pk>', SellInOutGetDeleteUpdateView.as_view(), name='sell-in-out-detail'),
    path('sell-in/', SellInListCreateView.as_view(), name='sell-in'),
    path('sell-in/<int:pk>', SellInGetDeleteUpdateView.as_view(), name='sell-in-detail'),
    path('sell-out/', SellOutListCreateView.as_view(), name='sell-out'),
    path('sell-out/<int:pk>', SellOutGetDeleteUpdateView.as_view(), name='sell-out-detail'),

]
