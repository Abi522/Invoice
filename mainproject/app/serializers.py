from rest_framework import serializers
from .models import Invoice
from .models import  Invoice_Detail

"""class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = "__all__"

class Invoice_DetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice_Detail
        fields = "__all__"
"""

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = ['Invoice_id', 'Customer_Name', 'Date']


class  Invoice_DetailSerializer(serializers.HyperlinkedModelSerializer):
    invoice_1 = InvoiceSerializer()

    class Meta:
        model = Invoice_Detail
        fields = "__all__"