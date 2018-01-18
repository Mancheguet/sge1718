#!/bin/sh
#Javier Moreno

clear
contador=10

echo '<odoo><data>' > caragols.xml

#Para que funcione , las imagenes tienen que ser .jpg y , estaran nombradas así : nombreCaracol_claseCaracol.jpg
for i in *.jpg; do
    #El nombre de las imagenes será para determinar los datos siguientes :
    name="$(echo $i | cut -d"_" -f1)" #El nombre se determina por la primera parte del nombre de la imagen
    idsnail=$contador
    contador=$[$contador+10]
    #snailsclass="$(echo $i | cut -d"_" -f2 | cut -d"." -f1)" #La segunda parte sin el punto de jpg es la clase
    description="Default description" #POr default , se escribirá esta descripción
    photo="$(base64 $i)" #Photo del caracol en base 64
    echo -e  '<record id="'$idsnail'" model="fastsnail.snail">\n<field name="name">'$name'</field>\n<field name="idsnail">'"$idsnail"'</field>\n<field name="description">'$description'</field>\n<field name="photo">'"$photo"'</field></record>' >> caragols.xml

done

echo '</data></odoo>' >> caragols.xml
