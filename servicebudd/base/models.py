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
    
class Filter(models.Model):
    category = models.CharField(max_length=100, null=True, blank= True)
    location = models.CharField(max_length=100, null=True, blank= True)
    starting_price = models.CharField(max_length=100, null=True, blank= True)

    def __str__(self):
        return f"{self.category} - {self.location} - {self.starting_price}"