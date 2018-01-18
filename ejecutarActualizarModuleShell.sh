#!/bin/bash
#Javier Moreno

#Ejecuta actualizando el modulo puesto a continuacion.
#Igual que tambien tenemos que poner la empresa a ejecutar

odoo shell --config /var/lib/odoo/.odoo_serverrc -d FastSnail -u fastsnail --save
