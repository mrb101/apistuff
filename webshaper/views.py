from django.shortcuts import render
from django.contrib.auth.models import User, Group
from api.serializers import UserSerializer, GroupSerializer
from serializers import CustomerSerializer, AddressSerializer, CustomerSerializer, AddressSerializer, CategorySerializer, ProductSerializer, ModifierSerializer, VariationSerializer, OrderSerializer, OrderItemSerializer, BrandSerializer
from rest_framework import viewsets
from rest_framework import routers
from .models import Customer, Address, Customer, Address, Category, Product, Modifier, Variation, Order, OrderItem, Brand


# ViewSets define the view behavior.
# API endpoint that allows users to be viewed or edited.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# API endpoint that allows Group to be viewed or edited.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# API endpoint that allows Customer to be viewed or edited.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# API endpoint that allows Address to be viewed or edited.
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

# API endpoint that allows Address to be viewed or edited.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# API endpoint that allows Address to be viewed or edited.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# API endpoint that allows Address to be viewed or edited.
class ModifierViewSet(viewsets.ModelViewSet):
    queryset = Modifier.objects.all()
    serializer_class = ModifierSerializer

# API endpoint that allows Address to be viewed or edited.
class VariationViewSet(viewsets.ModelViewSet):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer

# API endpoint that allows Address to be viewed or edited.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# API endpoint that allows Address to be viewed or edited.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# API endpoint that allows Address to be viewed or edited.
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer