from django.db import migrations

def add_sample_data(apps, schema_editor):
    Product = apps.get_model('myapp', 'Product')
    Product.objects.create(name='Product 1', price=19.99, quantity=50)
    Product.objects.create(name='Product 2', price=29.99, quantity=30)
    Product.objects.create(name='Product 3', price=9.99, quantity=100)

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_data),
    ]
