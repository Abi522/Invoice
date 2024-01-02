from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Invoice(models.Model):
    Invoice_id=models.BigAutoField(primary_key=True)
    Customer_Name = models.CharField(max_length=255)

    Date=models.DateTimeField(auto_now=True)


    def __str__(self):
          return self. Customer_Name


class Invoice_Detail(models.Model):
    invoice_1 = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    Description=models.TextField(max_length=255)
    quantity=models.TextField(blank=True,null=True)
    unit_price=models.TextField(blank=True,null=True)
    price=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.Description
