import re
import getpass
import requests
#import sqlite
import json

#while True:
    #barcode = raw_input("Escanear: ")

    #if re.match('TID.', barcode):
	 #   print "Es TingoID"
	#else:
	#	print "NO"
    #1. Preguntar a TingoID si el usuario existe

    #2. Consultar si tiene tinkets asociados a la empresa
    #3. Consultar cual ocupar <- recibir respuesta
    #response = 'response'
    #4. Mandar query a base de datos de la empresa
    #	a- Si no hay respuesta, ticket invalido
    #	b- Si hay respuesta ok, validar. (trigger) enviar actualizacion a TingoID
    #5. Mostrar el ticket validado o invalidado
    #print "Codigo escaneado: " + barcode


val = re.compile('^TID[0-9a-f]{24}$')

while True:
	#Paso 1
  cod = getpass.getpass('ESCANEAR CODIGO: ')
  if re.match('exit',cod): 
  	print 'Adios'
  	break

  if val.match(cod):
    #print 'Puede ser TingoID'
    #Paso 2
    #Hacer query a base de datos Tingo para consultar dada una empresa
    url = "http://localhost:8000/usarEntrada/" + cod
    test = "http://httpbin.org/post"
    myResponse = requests.post(test,data={'key':'value'})
    if (myResponse.ok):
    	print "Tinket: " + str(myResponse.headers)
    	#Recibimos un id correspondiente a ticket
    	#procede a validar en la base de datos de la empresa
    	
    else: 
    	print "No se encontraron tinkets asociados"
  else:
    print 'El ticket escaneado no es valido'