#!/bin/bash

echo "Dime el nombre del moudlo"
read nombre
#comando para crear un modulo
odoo scaffold "$nombre" 

