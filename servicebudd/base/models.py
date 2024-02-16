from django.db import models

# Create your models here.

class ServiceProvider(models.Model):
    category_choices = [
        ("Dining", "Dining"),
        ("Health", "Health"),
        ("Leisure", "Leisure"),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    starting_price = models.CharField(max_length=100)
    category = models.TextField(choices=category_choices)

    def __str__(self):
        return self.name