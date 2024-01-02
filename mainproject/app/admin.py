from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app.models import Invoice, Invoice_Detail

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Invoice_Detail)