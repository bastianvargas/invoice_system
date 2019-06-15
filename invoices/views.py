"""Invoices views."""

from django.shortcuts import render
from datetime import datetime
from invoices.models import Invoice
from xml.etree import ElementTree as ET

def home(request):
    return render(request, 'invoices/home.html')

def list_invoice(request):

    invoices = Invoice.objects.all().order_by('-date')
    for i in invoices:

        a = i.detail.split(',')
        print(a)

    return render(request, 'invoices/list_invoice.html', { 'invoices': invoices})

def load_invoice(request):
    variables = {}
    if request.POST:
        invoice = Invoice()
        detail_invoice = []
        xmlfile = request.FILES['xmlfile']
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        emision = int(root.attrib['emision'])
        emision = datetime.utcfromtimestamp(emision).strftime('%Y-%m-%d')
        invoice.date = emision
        tipo = root.attrib['tipo']
        invoice.type = tipo
        folio = root.attrib['folio']
        invoice.folio = int(folio)
        rut_emisor = root[0].attrib['rut']
        invoice.issuing_rut = str(rut_emisor)
        nombre_emisor = root[0].attrib['razonSocial']
        invoice.issuing_name = nombre_emisor
        rut_receptor = root[1].attrib['rut']
        invoice.receiver_rut = str(rut_receptor)
        nombre_receptor = root[1].attrib['razonSocial']
        invoice.receiver_name = nombre_receptor
        detail = []
        for r in root[2]:
            dic = {
                    'monto': r.attrib['monto'],
                    'iva': r.attrib['iva'],
                    'detalle': r.text
            }
            detail.append(dic)
        invoice.detail = str(detail)
        try:
            invoice.save()
            variables['mensaje'] = "guardado correctamente"
            print("se guardo")
        except:
            variables['mensaje'] = "error al guardar"
            print("no se guardo")

    return render(request, 'invoices/load_invoice.html', variables)
