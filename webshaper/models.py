from django.db import models


# Customer Model
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return u'%s %s' % (self.first_name, self.last_name)


# Address Model. reference for other tables
class Address(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    addressline1 = models.CharField(max_length=200)
    addressline2 = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    extra = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):  # __str__ on Python 3
        return u'%s %s' % (self.first_name, self.last_name)


# Category. self reference through the frontend
class Category(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)
    title = models.CharField(max_length=30)
    parent = models.IntegerField()  #self reference field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return u'%s %s' % (self.name, self.title)


# Product Model.
class Product(models.Model):
    # Choices is productstatus choices.
    LIVE = 'Live'
    DRAFT = 'Draft'
    CHOICES = (
        (LIVE, 'Live'),
        (DRAFT, 'DRAFT'),
    )
    # Status is stockstatus choices.
    INSTOCK = 'In Stock'
    LOWSTOCK = 'Running Out'
    OUTOFSTOCK = 'Out of Stock'
    DISCONTINUED = 'Discontinued'
    ORDERED = 'Ordered'
    STATUS = (
        (INSTOCK, 'In Stock'),
        (LOWSTOCK, 'Running Out'),
        (OUTOFSTOCK, 'No Stock'),
        (DISCONTINUED, 'Discontinued'),
        (ORDERED, 'Ordered'),
    )
    sku = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=30, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    saleprice = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        )
    productstatus = models.CharField(
        max_length=10,
        choices=CHOICES,
        default=DRAFT,
        )
    stockstatus = models.CharField(
        max_length=30,
        choices=STATUS,
        default=INSTOCK,
        )
    stocklevel = models.IntegerField()
    description = models.CharField(max_length=200)
    shipping = models.BooleanField(default=True)
    weight = models.DecimalField(max_digits=5, decimal_places=5)
    height = models.DecimalField(max_digits=5, decimal_places=5)
    width = models.DecimalField(max_digits=5, decimal_places=5)
    depth = models.DecimalField(max_digits=5, decimal_places=5)
    category = models.ForeignKey(Category) # Category table
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return u'%s %s' % (self.title, self.description)


# Modifier Table. reference to product. and has many (variations.Model).
class Modifier(models.Model):
    title = models.CharField(max_length=30)
    product = models.ForeignKey(Product) # Product Model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return self.title


# Variation Model.. Refence to Modifier and Product.
class Variation(models.Model):
    title = models.CharField(max_length=30)
    pricemod = models.DecimalField(max_digits=5, decimal_places=2)
    modifier = models.ForeignKey(Modifier) # Modifier Model
    product = models.ForeignKey(Product) # Product Model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return self.title


# Brand Model.
class Brand(models.Model):
    LIVE = 'Live'
    DRAFT = 'Draft'
    BRAND = (
        (LIVE, 'Live'),
        (DRAFT, 'Draft'),
    )
    slug = models.SlugField(max_length=30, unique=True)
    status = models.CharField(
        max_length=20,
        choices=BRAND,
        default=DRAFT,
        )
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    product = models.IntegerField() # Product Model
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 'Magic Method'Helps to view instances of a django model.
    def __unicode__(self):  # __str__ on Python 3
        return self.name


# Order Model.
class Order(models.Model):
    INCOMPLETE = 'Incomplete'
    PENDING = 'Pending'
    PROCESSED = 'Processed'
    SHIPPED = 'Shipped'
    CANCELED = 'Canceled'
    ORDER = (
        (INCOMPLETE, 'Order is Incomplete'),
        (PENDING, 'Order is Pending'),
        (PROCESSED, 'Order is Processed'),
        (SHIPPED, 'Order is Shipped'),
        (CANCELED, 'Order is Canceled'),
    )
    customer = models.ForeignKey(Customer) # Customer Model
    orderstatus = models.CharField(
        max_length=20,
        choices=ORDER,
        default='',
        )
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    shippingprice = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    shipto = models.IntegerField(null=True) # Reference to Address
    billto = models.IntegerField(null=True) # Reference to Address
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Order Item Model.. Many to Many node (Product -> OrderItem <- Order)
class OrderItem(models.Model):
    order = models.IntegerField() # Order Model
    product = models.IntegerField() # Product Model
    sku = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField()
    taxrate = models.DecimalField(max_digits=5, decimal_places=2)
    taxband = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)