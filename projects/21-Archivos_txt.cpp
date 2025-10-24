//Crear un archivo
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    //Creando un archivo
    ofstream Mi_archivo("Archivo_de_texto.txt");
    //Escribiendo en el archivo
    Mi_archivo<<"Hola mundo, este es un archivo de texto";
    //Cerrando el archivo
    Mi_archivo.close();
    //Crear una variable para ver el archivo
    string Leermiarchivo;
    //Leer desde el documento de texto
    ifstream Mi_archivo_leer("Archivo_de_texto.txt");
    //Usar un whileloop junto con el getline() para leer el archivo line por linea
    while (getline(Mi_archivo_leer,Leermiarchivo)){
        //Mostrar el texto de mi archivo
        cout<<Leermiarchivo;
    }
    return 0;
}
