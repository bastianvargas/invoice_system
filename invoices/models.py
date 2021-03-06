"""Invoices models."""

#django
from django.db import models

class Invoice(models.Model):
    """Invoice model.
    Invoice model is a representation of file invoice xml
    previously loaded"""

    date = models.DateField()
    type = models.CharField(max_length=10)
    folio = models.IntegerField()
    issuing_rut = models.CharField(max_length=15)
    issuing_name = models.CharField(max_length=30)
    receiver_rut = models.CharField(max_length=15)
    receiver_name = models.CharField(max_length=30)
    detail = models.TextField()

    def __str__(self):
        return str(self.date)+ " - " +str(self.type)+ " - " +str(self.folio)+ " - " +str(self.issuing_rut)+ " - " +str(self.issuing_name)+ " - " +str(self.receiver_rut)+ " - " +str(self.receiver_name)+ " - " +str(self.detail)
