

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import  Invoice_DetailViewSet,InvoiceViewSet
from app import views

router = routers.DefaultRouter()
router.register(r'invoice', Invoice_DetailViewSet),
#router.register(r'Invoice_Detail', Invoice_DetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('pp/', views.home, name='pp')

]

















"""urlpatterns = [
    path('', views.getInvoice),
    path ('create', views.add_Invoice),
    path ('update/<str:pk>', views.update_Invoice),
    path('read/<str:pk>', views.getInvoice),
    path ('delete/<str:pk>', views.deleteInvoice),
    path ('creat/<str:pk>', views.add_Invoice_Detail),
    path ('update/<str:pk>', views.update_Invoice_Detail),
]"""