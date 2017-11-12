from django.db import models


class Node(models.Model):
    name = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
