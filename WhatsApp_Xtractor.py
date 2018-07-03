# -*- coding: utf-8 -*-

import re
import os
from os import getcwd

print ("Whatsapp Xtractor")

directorio = getcwd()
archivo = open(directorio+"\\WhatsApp.htm",'r',encoding = "ANSI")
contenido = archivo.read()

patron_telefonos = re.compile("\W{1}\d{2}&nbsp;9&nbsp;\d{2}&nbsp;\d{4}[ -]?\d{4}")

lista = re.findall(patron_telefonos, contenido)
resultado = list(set(lista))

f = open('celulares.txt','w')

for i in resultado:
    num = i.replace("&nbsp;"," ")
    f.write(num+'\n')
    print (num)
    
f.write("Total de Numeros extraidos: "+str(len(resultado)))
print (len(resultado))    
print("Listo")

f.close()
archivo.close()
os.startfile("celulares.txt")
