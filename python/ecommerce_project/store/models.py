from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to= 'products/')
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
#Model for Order
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True,default=00)
    products = models.ManyToManyField(Product, through="OrderItem", related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled')
    ],
        default="pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem.set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items", blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return f"Cart for {self.customer.name}"
    
    @property
    def get_cart_total(self):
        total = sum([item.get_total for item in self.items.all()])
        return total
    
    @property
    def get_cart_items(self):
        total = sum([item.quantity for item in self.items.all()])
        return total
    

    
# class Order(models.Model):
#         customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
#         date_ordered = models.DateTimeField(default=timezone.now)
#         complete = models.BooleanField(default=False)
#         transaction_id = models.CharField(max_length=100, null=True)

#         def __str__(self):
#             return str(self.transaction_id)
    
#         @property
        
#         def get_cart_total(self):
#             orderitems = self.orderitem.set.all()
#             total = sum([item.get_total for item in orderitems])
#             return total
        
#         @property
#         def get_cart_items(self):
#             orderitems = self.orderitem_set.all()
#             total = sum([item.quantity for item in orderitems])
#             return total
    