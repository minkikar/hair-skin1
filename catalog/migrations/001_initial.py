from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150)),
                ("category", models.CharField(choices=[("skincare", "Skincare"), ("haircare", "Haircare")], max_length=30)),
                ("product_type", models.CharField(max_length=120)),
                ("description", models.TextField()),
                ("ingredients", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("image", models.ImageField(blank=True, null=True, upload_to="products/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Recommendation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("category", models.CharField(choices=[("skincare", "Skincare"), ("haircare", "Haircare")], max_length=30)),
                ("concerns", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("recommended_products", models.ManyToManyField(related_name="recommendations", to="catalog.product")),
            ],
        ),
    ]