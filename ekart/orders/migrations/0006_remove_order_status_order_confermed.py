# Generated by Django 5.0.6 on 2024-06-10 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_id_alter_order_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='confermed',
            field=models.BooleanField(default=False),
        ),
    ]
