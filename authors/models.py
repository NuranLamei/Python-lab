from django.db import models

# Create your models here.
class Author(models.Model):
    auth_name = models.CharField(max_length = 100)
    auth_ID = models.AutoField(primary_key=True)

