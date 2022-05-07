from django.db import models


# Create your models here.
class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

