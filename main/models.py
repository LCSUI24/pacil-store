import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pakaian', 'Pakaian'),
        ('exclusive', 'Exclusive'),
        ('elektronik', 'Elektronik'),
        ('makanan', 'Makanan'),
        ('minuman', 'Minuman'),
        ('aksesoris', 'Aksesoris'),
        ('trend', 'Trend'),

    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    product_views = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
    def increment_views(self):
        self.product_views += 1
        self.save()