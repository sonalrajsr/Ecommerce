# Generated by Django 5.0.6 on 2024-06-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featured_Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(upload_to='featured_images/')),
            ],
        ),
        migrations.CreateModel(
            name='New_arrival',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('image', models.ImageField(upload_to='newarrival_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]