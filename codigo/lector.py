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
lista = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299]


def feria(cod):
  if re.match('Feria .',cod):
    tinket = int(cod[6:])
    if (tinket in lista):
      lista.remove(tinket)
      return ("Código N°"+str(tinket)+" validado correctamente")
    else:
      return ("El código "+str(tinket)+" ya fue utilizado")
  return ("El código escaneado no corresponde a TingoID")

def lector(cod):
#while True:
	#Paso 1
  #cod = getpass.getpass('ESCANEAR CODIGO: ')
  if cod == '':
    return ("Esperando...",5)
  tinket = cod[4:]

  #No se si implementar esta funcion, quizas para un cierre forzado y necesario
  
  if re.match('CASINO.',cod):
  	return ("El codigo no pertenece a \nTingoID, pero puede \nser valido",2)

  elif re.match('TID.',cod):
    #return ("Tinket pertenece a TingoID,\npuede ser valido",1)
    #print 'Puede ser TingoID'
    #Paso 2
    #Hacer query a base de datos Tingo para consultar dada una empresa
    url ='http://'+'10.6.43.137:8000'+'/tingo/usarEntrada/'
    #url = 'http://'+empresa.ip+empresa.puerto+'/'+empresa.nombre+'/detalle'
    data = {'id_usuario': tinket,
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