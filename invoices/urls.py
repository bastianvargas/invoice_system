from django.urls import path
from .views import home, load_invoice, list_invoice

urlpatterns = [
    path('', home, name="home"),
    path('load_invoice/', load_invoice, name="load_invoice"),
    path('list_invoice/', list_invoice, name="list_invoice")
]
