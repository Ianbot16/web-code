//Crear clase
#include<iostream>
#include<string>
using namespace std;
class Registro {
    public:
      string cedula;
      string nombre;
      string apellido;
      int edad;
      string genero;
      string nacionalidad;

};

int main(){
  Registro datos;
  cout<<"Ingrese su numero de cedula: ";
  cin>>datos.cedula;
  cout<<"Ingrese sus nombres: ";
  cin>>datos.nombre;
  cout<<"Ingrese sus apellidos: ";
  cin>>datos.apellido;
  cout<<"Ingrese la edad: ";
  cin>>datos.edad;
  cout<<"Ingrese su sexo: ";
  cin>>datos.genero;
  cout<<"Ingrese su nacionalidad: ";
  cin>>datos.nacionalidad;

  cout<<"N. de cedula: "<< datos.cedula<<endl;
  cout<<"Nombres: " << datos.nombre << endl;
  cout<<"Apellidos: "<<datos.apellido<<endl;
  cout<<"Edad: "<<datos.edad<<endl;
  cout<<"Genero: "<<datos.genero<<endl;
  cout<<"Nacionalidad: "<<datos.nacionalidad<<endl;
  return 0;
}