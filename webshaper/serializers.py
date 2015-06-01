from django.forms import widgets
from rest_framework import serializers
from .models import Customer, Address, Category, Product, Modifier, Variation, Brand, Order, OrderItem

# Serializers define the API representation.
class CustomerSerializer(serializers.Serializer):
      class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'email', 'updated_at')

class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'addressline1', 'addressline2', 'country', 'city', 'postcode')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Category
    	fields = ('name', 'slug', 'title', 'parent', 'created_at', 'updated_at')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Product
        fields = ('sku', 'title', 'slug', 'price', 'saleprice', 'productstatus', 'stockstatus', 'stocklevel', 'description', 'shipping', 'shipping', 'weight', 'height', 'width', 'depth', 'created_at', 'updated_at')


class ModifierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Modifier
    	fields = ('title', 'product', 'created_at', 'updated_at')


class VariationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Variation
    	fields = ('title', 'pricemod', 'modifier', 'product', 'created_at', 'updated_at')

class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Brand
    	fields = ('slug', 'status', 'name', 'description', 'product', 'created_at', 'updated_at')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = Order
    	fields = ('customer', 'orderstatus', 'subtotal', 'shippingprice', 'total', 'shipto', 'billto', 'created_at', 'updated_at')


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    	model = OrderItem
    	fields = ('order', 'product', 'sky', 'quantity', 'taxrate', 'taxband', 'price', 'created_at', 'updated_at')