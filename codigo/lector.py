import re
import getpass
import requests
import json
import ipaddress

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
ip_apitingo = ipaddress.ip_address('10.6.43.164') #Ip API de Tingo
id_empresa = 1 #Asignar el id correspondiente a la empresa asociada a esta estacion de TingoID
val = re.compile('^TID.')
nti = re.compile('^CASINO.')

def lector(cod):
#while True:
	#Paso 1
  #cod = getpass.getpass('ESCANEAR CODIGO: ')
  tinket = cod[3:]
  #No se si implementar esta funcion, quizas para un cierre forzado y necesario
  if re.match('exit',cod): 
  	return ("Programa Finalizado",3)
  
  elif re.match('CASINO.',cod):
  	return ("El codigo no pertenece a \nTingoID, pero puede \nser valido",2)

  elif re.match('TID.',cod):
    #return ("Tinket pertenece a TingoID,\npuede ser valido",1)
    #print 'Puede ser TingoID'
    #Paso 2
    #Hacer query a base de datos Tingo para consultar dada una empresa
    url ='http://'+'10.6.43.212:8000'+'/tingo/usarEntrada/'
    #url = 'http://'+empresa.ip+empresa.puerto+'/'+empresa.nombre+'/detalle'
    data = {'id_usuario': 3,
            'id_empresa': 1 }
    datajson = json.dumps(data)
    response = requests.post(url, data=datajson) #json.dumps(data))
    response_data = json.loads(response.text)
    discount = str(response_data['discount'])
    mensaje = str(response_data['mensaje'])
    
    if (response.ok):
    	return (mensaje,"green")
    	#Recibimos un id correspondiente a ticket
    	#Procede a validar en la base de datos de la empresa
    	#Este mensaje lo manda la API de TingoID
    	
    else: 
    	return ("Error Fatal")#Este error no existe, ya que si no se almacena la APITingo nos envia ese mensaje.'''
  
  else:
    return ("El codigo escaneado \nNO pertenece a TingoID,\nvuelva a escanear un \ncodigo valido",0)