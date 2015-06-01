"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from webshaper import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api/v01/users', views.UserViewSet)
router.register(r'api/v01/groups', views.GroupViewSet)
router.register(r'api/v01/customer', views.CustomerViewSet)
router.register(r'api/v01/address', views.AddressViewSet)
router.register(r'api/v01/category', views.CategoryViewSet)
router.register(r'api/v01/product', views.ProductViewSet)
router.register(r'api/v01/modifier', views.ModifierViewSet)
router.register(r'api/v01/variation', views.VariationViewSet)
router.register(r'api/v01/brand', views.BrandViewSet)
router.register(r'api/v01/order', views.OrderViewSet)
router.register(r'api/v01/orderitem', views.OrderItemViewSet)



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]