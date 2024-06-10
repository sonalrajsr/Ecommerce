from django.db import models
from django.contrib.auth.models import User
from products.models import Featured_Product
import uuid

class Order(models.Model):
    id = models.AutoField(primary_key=True, default=None)
    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Featured_Product, on_delete=models.CASCADE)
    confermed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.order_id} by {self.user.username}'
