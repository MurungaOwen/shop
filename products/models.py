from django.db import models


class Product(models.Model):
    """Products added by client"""
    name = models.CharField(max_length = 20)
    category = models.TextField()
    image = models.FileField(upload_to = "products/")
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name + '\t@{} for {}'.format(self.price, self.category)
