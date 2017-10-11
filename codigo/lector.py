import re
import getpass
import psycopg2

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


val = re.compile('TID.')

while True:
	#Paso 1
  cod = getpass.getpass('Escanear codigo: ')
  if re.match('exit',cod): 
  	print 'Adios'
  	break

  if val.match(cod):
    print 'Es TingoID'
    #Paso 2
    #Hacer query a base de datos Tingo para consultar dada una empresa
  else:
    print 'NO'