from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from buildings.models import Material


class Organization(models.Model):
    name = models.CharField(unique=True, max_length=254)
    members = models.ManyToManyField(
        User,
        through='Membership',
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    material_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = (("user", "organization"),)


class StockMaterial(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    count = models.IntegerField()
