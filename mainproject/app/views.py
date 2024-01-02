from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import  Invoice
from .serializers import InvoiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Invoice_Detail
from .serializers import Invoice_DetailSerializer
from rest_framework import viewsets
from app.models import Invoice, Invoice_Detail
from django.shortcuts import render
"""@api_view(['GET'])
def getData(request):
    invoice =  Invoice.objects.all()
    serializer =  InvoiceSerializer(invoice, many=Tobjectrue)
    return Response(serializer.data)

@api_view(['GET'])
def get_Invoice(request, pk):
    invoice =  Invoice.objects.get(id=pk)
    serializer =  InvoiceSerializer(invoice, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def add_Invoice(request):
    serializer =  InvoiceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(['GET'])
def getInvoice(request):
    invoice = Invoice.objects.all()
    serializer = InvoiceSerializer(invoice, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_Invoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    serializer = InvoiceSerializer(instance=invoice, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
@api_view(['DELETE'])
def deleteInvoice(request, pk):
    invoice = Invoice.objects.get(id=pk)
    invoice.delete()
    return Response('User successfully deleted!')


@api_view(['POST'])
def add_Invoice_Detail(request):
    serializer = Invoice_DetailSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def update_Invoice_Detail(request, pk):
    invoice_Detail = Invoice_Detail.objects.get(id=pk)
    serializer = Invoice_Detail(instance=invoice_Detail, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)"""


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer

class  Invoice_DetailViewSet(viewsets.ModelViewSet):
    queryset=Invoice_Detail.objects.all()
    serializer_class= Invoice_DetailSerializer