# Generated by Django 5.0.6 on 2024-06-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='massage',
            field=models.TextField(),
        ),
    ]
