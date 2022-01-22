from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, null=False, blank=False)
    description1 = models.CharField(max_length=256, null=False, blank=False)
    description2 = models.CharField(max_length=256, null=True, blank=True)
    description3 = models.CharField(max_length=256, null=True, blank=True)
    description4 = models.CharField(max_length=256, null=True, blank=True)
    description5 = models.CharField(max_length=256, null=True, blank=True)
    description6 = models.CharField(max_length=256, null=True, blank=True)
    description7 = models.CharField(max_length=256, null=True, blank=True)
    description8 = models.CharField(max_length=256, null=True, blank=True)
    description9 = models.CharField(max_length=256, null=True, blank=True)
    description10 = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        return self.title
