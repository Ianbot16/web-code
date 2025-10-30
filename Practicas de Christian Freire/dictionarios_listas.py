import random
usuario={
    "cedula":" ",
    "nombres":" ",
    "apellidos":" ",
    "sexo":" ",
    "fecha de Naciminto":" ",
    "edad": 0
    }

lista=[]

lista.append( {"cedula": "0954343208", "nombres":"Christian Javier","apellidos":"Freire Baquero","sexo":"Masculino","edad":20})
lista.append( {"cedula": "0984582392", "nombres":"Jacinta Fabiana","apellidos":"Guerrero Vasconez","sexo":"Femenino","edad":24})
lista.append( {"cedula": "0960968343", "nombres":"Marcos Julian ","apellidos":"Padilla Suarez","sexo":"Masculino","edad":22})
lista.append( {"cedula": "0946873267", "nombres":"Horacio Franciscco","apellidos":"García Lopez","sexo":"Masculino","edad":19})
lista.append( {"cedula": "0954845987", "nombres":"María Amanda","apellidos":"Carvajal Fernandez","sexo":"Femenino","edad":30})
lista.append( {"cedula": "0903149294", "nombres":"Kiara Inez","apellidos":"Fernandez Vasconez","sexo":"Femenino","edad":23})
lista.append( {"cedula": "0909540498", "nombres":"Jaime Benito","apellidos":"Guevara Robles","sexo":"Masculino","edad":27})
lista.append( {"cedula": "0993932209", "nombres":"Ramona Anastasia ","apellidos":"Perez Robayo","sexo":"Femenino","edad":25})


#buscar = input("Introduce una cedula: \r\n")
#for u in lista:
 #   if buscar == u["cedula"]:
  #      print("-----------------")
   #     print("Cedula: ",u["cedula"])
    #    print("Nombres: ",u["nombres"])
     #   print("Apellidos: ",u["apellidos"])
      #  print("Sexo: ",u["sexo"])
       # print("Edad: ",u["edad"])
    #else:
     #   print("No existe esa cedula")
for u in lista:   
    primera_persona=(random.choice(lista))
    segunda_persona=(random.choice(lista))
    print(primera_persona)
    print(segunda_persona)
    if primera_persona["sexo"] == segunda_persona["sexo"]:
        print("Ellos no pueden estar juntos")
        break
    else:
        print("Ellos si pueden estar juntos")
        print("Han sido unidos")
        print(primera_persona["nombres"])
        print("y")
        print(segunda_persona["nombres"])
        