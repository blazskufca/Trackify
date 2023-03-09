from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TrackedProducts(models.Model):
    name = models.CharField(max_length=500, null=False, unique=True, blank=False)
    link = models.TextField(db_index=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    priceHistory = models.JSONField()
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(TrackedProducts)

    def __str__(self):
        return self.user.username
