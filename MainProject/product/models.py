from django.db import models

# Model for Bike Brand
class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # database table name in mysql xampp server
        db_table = 'brands'

    def __str__(self):
        return self.name

# Model for Bike Category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # database table name in mysql xampp server
        db_table = 'category'

    def __str__(self):
        return self.name




# Model for Bike
# In models.py
class Laptop(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='laptops/', blank=True, null=True, default='static/images/bg1.png')

    class Meta:
        db_table = 'laptop'

    def __str__(self):
        return self.name

