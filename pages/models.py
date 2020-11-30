from django.db import models


# Tags
class Tag(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


# Products
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(null=True, blank=True, upload_to="")
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
