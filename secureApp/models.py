from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


class Software(models.Model):
    name = models.CharField(max_length=100)
    devlopedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SecureHub(models.Model):
    portName = models.CharField(max_length=100)
    handledBy = models.ForeignKey(User, on_delete=models.CASCADE)
    secKey = models.IntegerField(null=False, blank=False)
    linkedSoft = models.ForeignKey(Software, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.portName
