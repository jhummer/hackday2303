from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=64)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
