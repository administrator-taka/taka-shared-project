from django.db import models

class Test(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
