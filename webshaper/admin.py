from django.contrib import admin
from .models import Product, Modifier, Variation, OrderItem, Order, Brand, Category, Customer, Address


admin.site.register(Product)
admin.site.register(Modifier)
admin.site.register(Variation)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Address)

'''
class ProductAdmin(Admin.ModelAdmin):
	pass


class ModifierAdmin(Admin.ModelAdmin):
	pass


class VariationAdmin(Admin.ModelAdmin):
	pass


class OrderItemAdmin(Admin.ModelAdmin):
	pass


class OrderAdmin(Admin.ModelAdmin):
	pass


class BrandAdmin(Admin.ModelAdmin):
	pass


class CategoryAdmin(Admin.ModelAdmin):
	pass


class CustomerAdmin(Admin.ModelAdmin):
	pass	


class AddressAdmin(Admin.ModelAdmin):
	pass						
'''