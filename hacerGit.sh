#!/bin/bash
#Javier Moreno

#hacer git de toda la carpeta
git add *
#hacer commit - cambiar el mensaje por el que queremos
#Parte comentario automatico
echo 'Dime el mensaje para el commit : '
read nombre

git commit -m $nombre
#descomentar esta linea para crear el origin
git remote add origin1 https://github.com/Mancheguet/sge_17_18_treball.git
#hacer el push para subir los archivos
git push -u origin1 master
