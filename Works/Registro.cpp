//Crear un registro de usuarios
#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
#include <direct.h>
using namespace std;



int menu(){
    int x;
    cout<<"\n";
    cout<<"Registro de usuario"<<endl;
    cout<<"Elija una opción: "<<endl;
    cout<<"1) Ingrese un usuario"<<endl;
    cout<<"2) Modifique un usuario"<<endl;
    cout<<"3) Elimine un usuario"<<endl;
    cout<<"4) Mustre los registros"<<endl;
    cout<<"5) Salir"<<endl;
    cout<<"Ingrese un número: ";
    cin>>x;
    return x;
}

bool verificar_usuario(string Ced){
    ifstream leer_registro("Registro.txt",ios::in);
    string ced, nom, ape,tel,sexo;
    int edad;
    leer_registro>>ced;
    while (!leer_registro.eof())
    {
        leer_registro>>nom;
        leer_registro>>ape;
        leer_registro>>edad;
        leer_registro>>sexo;
        leer_registro>>tel;
        if (ced==Ced){
            cout<<"Este usuario ya existe";
            leer_registro.close();
            return false;
        }
        leer_registro>>ced;

        
    }
    cout<<"Ingresando nuevo usuario";
    leer_registro.close();
    return true;
    

}

void agregar_usuario(ofstream &es){
    system("cls");
    setlocale(LC_ALL,"");
    string ced,nom,ape,sexo,tel;
    int edad;
    es.open("Registro.txt",ios::out| ios::app);
    cout<<"Ingrese su número cédula: ";
    cin>>ced;
    cout<<"Ingrese su nombre: ";
    cin>>nom;
    cout<<"Ingrese su apellido: ";
    cin>>ape;
    cout<<"Ingrese su edad: ";
    cin>>edad;
    cout<<"Ingrese su género: ";
    cin>>sexo;
    cout<<"Ingresé su número de teléfono: ";
    cin>>tel;
    if (verificar_usuario(ced))
       es<<"-------------------"<<"\n"<<"Número de cédula: "<<ced<<"\n"<<"Nombres: "<<nom<<"\n"<<"Apellidos: "<<ape<<"\n"<<"Edad: "<<edad<<"\n"<<"Género: "<<sexo<<"\n"<<"Teléfono: "<<tel<<"\n"<<"--------------------"<<"\n";
    es.close();

}

void modificar_usuario();

void eliminar_usuario();

void buscar_usuario();

void mostrar_usuarios();

int main(){
    system("cls");
    setlocale(LC_ALL,"");
    ofstream Esc;
    int op;
    do
    {
        op=menu();
        switch (op)
        {
        case 1:
            agregar_usuario(Esc);
            break;
        case 2:
            //modificar_usuario();
            break;
        case 3:
            //elimine_usuario();
            break;
        case 4:
            //buscar_usuario();
            break;
        case 5:
            //mostrar usuarios();
            break;
        case 6:
            cout<<"Saliendo del sistema"<<endl;
            break;
        default:
            //cout<<"Ingrese otro número";
            break;
        }
    } while (op != 6);
    
    
    return 0;
}