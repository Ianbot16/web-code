#include<iostream>
#include<cmath>
using namespace std;
int main(){
    setlocale(LC_ALL,"");
    double n1,n2,total;
    int opcion;
    do
    {
        cout<<"Calculadora"<<endl;
        cout<<"1) Suma de operaciones"<<endl;
        cout<<"2) Resta de operaciones"<<endl;
        cout<<"3) Multiplicaci�n de operaciones"<<endl;
        cout<<"4) Divisi�n de operaciones"<<endl;
        cout<<"5) Salir"<<endl;
        cout<<"Elija una opci�n: ";
        cin>>opcion;

        switch (opcion)
        {
        case 1:
            cout<<"Ingrese dos n�meros para sumar"<<endl;
            cout<<"Ingrese el primer n�mero: ";
            cin>>n1;
            cout<<"Ingrese el segundo n�mero: ";
            cin>>n2;
            total=n1+n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 2:
            cout<<"Ingrese dos n�meros para restar"<<endl;
            cout<<"Ingrese el primer n�mero: ";
            cin>>n1;
            cout<<"Ingrese el segundo n�mero: ";
            cin>>n2;
            total=n1-n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 3:
            cout<<"Ingrese dos n�meros para multiplicar"<<endl;
            cout<<"Ingrese el primer n�mero: ";
            cin>>n1;
            cout<<"Ingrese el segundo n�mero: ";
            cin>>n2;
            total=n1*n2;
            cout<<"El resultado es: "<<total<<endl;
            break;

        case 4:
            cout<<"Ingrese dos n�meros para dividir"<<endl;
            cout<<"Ingrese el primer n�mero: ";
            cin>>n1;
            cout<<"Ingrese el segundo n�mero: ";
            cin>>n2;
            total=n1/n2;
            cout<<"El resultado es: "<<total<<endl;
            break;
        
        case 5:
            cout<<"Saliendo del sistema"<<endl;
            break;

        default:
            cout<<"N�mero incorrecto, intente otro n�mero"<<endl;
            break;
        }
    } while (opcion!=5);
    return 0;
}