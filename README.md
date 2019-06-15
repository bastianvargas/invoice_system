## SISTEMA DE FACTURAS

sistema para la visualizacion de facturas mediante la carga de archivos xml

para levantar el proyecto es necesario ejecutar el comando


**python manage.py runserver**

no es necesario crear un super usuario ya que aun no se implementa un modulo de usuarios.

el sistema cuenta con 3 vistas

1. una vista Home **{servidor}/** donde muestra 2 opciones a seleccionar: listar facturas en la base de datos o cargar archivos xml

1. vista con una lista de facturas ordenadas por fecha de emision **{servidor}/list_invoice/** 

1. vista que permite cargar archivos XML para ser procesados **{servidor/load_invoice/}**




