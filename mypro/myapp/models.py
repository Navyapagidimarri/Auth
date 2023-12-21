from django.db import models


class Marolix_login(models.Model):
    username=models.CharField(primary_key=True,max_length=200)
    password=models.CharField(max_length=100)