from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Software(models.Model):
    name = models.CharField(max_length=100)
    devlopedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " | " + str(self.devlopedBy)


class SecureHub(models.Model):
    portName = models.CharField(max_length=100)
    handledBy = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="securehub")
    secKey = models.IntegerField(null=False, blank=False)
    linkedSoft = models.ForeignKey(Software, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)], default=3)
    licensed = models.BooleanField(default=True)

    def __str__(self):
        return self.portName + " | " + str(self.handledBy) + " | " + self.linkedSoft.name
