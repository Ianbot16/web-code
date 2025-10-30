def app():
    #Crear el archivo
    archivo=open("archivo.txt","w") #W es escritura, si no existe lo creara
    
    #Generar numeros en el archivo 
    for i in range(0,20):
        archivo.write("Esta es la linea"+ str(i) + "\r\n")
    
    #Cerrar el archivo para que no consuma más memoria
    archivo.close

app()