from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("skincare", "Skincare"),
        ("haircare", "Haircare"),
    ]

    name = models.CharField(max_length=150)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    product_type = models.CharField(max_length=120)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    CATEGORY_CHOICES = [
        ("skincare", "Skincare"),
        ("haircare", "Haircare"),
    ]

    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    concerns = models.TextField()
    recommended_products = models.ManyToManyField(Product, related_name="recommendations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.get_category_display()})"

@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(save=False)

@receiver(pre_save, sender=Product)
def cleanup_replaced_product_image(sender, instance, **kwargs):
    if not instance.pk:
        return
    try:
        previous = Product.objects.get(pk=instance.pk)
    except Product.DoesNotExist:
        return
    if previous.image and previous.image != instance.image:
        previous.image.delete(save=False)